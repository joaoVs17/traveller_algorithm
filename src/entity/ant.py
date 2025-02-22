from typing import List
from entity.graph import Graph
import random
from entity.npmatrix import Matrix
class Ant:  

  bestPath: List[int] = []
  bestPathDistance: float = -1

  def __init__(self, city: int):
    self.city: int = city
    self.travelling: bool = False
    self.lastPath: List[int] = []
    self.lastPathDistance: float = 0
    self.currentPath: List[int] = []
    self.currentPathDistance: float = 0

  def calcTravelProbability(self, cityA: int, cityB: int, graph: Graph, feromoneInfluence: float, visibilityInfluence: float):
    edgeFeromone: float = graph.scoreMatrix[cityA][cityB]
    edgeVisibility: float = 1/graph.matrix[cityA][cityB] if graph.matrix[cityA][cityB] != 0 else 0

    dividend: float = pow(edgeFeromone, feromoneInfluence) * pow(edgeVisibility, visibilityInfluence)

    divider: float = sum(
      pow(graph.scoreMatrix[cityA][col], feromoneInfluence) * 
      pow(1 / graph.matrix[cityA][col], visibilityInfluence) 
      for col in range(graph.matrix.columns) if col not in self.currentPath and col != cityA and graph.matrix[cityA][col] != 0
    )
    
    return dividend / divider if divider != 0 else 0

  def pickNextCity(self, graph: Graph, currentCity: int) -> int:
    
    probabilityObj: dict[int, float]  = {
      city: self.calcTravelProbability(currentCity, city, graph, 1, 2)
      for city in range(graph.matrix.columns)
      if city not in self.currentPath and city != currentCity
    }
    
    if not list(probabilityObj.keys()):
      return -1
    
    #Ideia: usar as probabilidades como teto de aceitação. Um número é randomizado e, caso esteja dentro desse teto é escolhido
    #Números maiores possuem, portanto, maior chance de serem escolhidos
    cities, probabilities = zip(*probabilityObj.items()) #Separando cidades de probabilidades
    return random.choices(cities, weights=probabilities, k=1)[0] #Python them função de escolha própria que leva em conta pesos
  
  def travel(self, graph: Graph) -> None:
    self.currentPath.append(self.city)
    
    while True:

      self.travelling = True
      nextCity: int = self.pickNextCity(graph, self.city)
    
      if (nextCity < 0):
        self.currentPathDistance += graph.matrix[self.city][self.currentPath[0]]
        self.city = self.currentPath[0]
        self.currentPath.append(self.currentPath[0])

        self.lastPath = self.currentPath
        self.lastPathDistance = self.currentPathDistance
        if self.lastPathDistance < Ant.bestPathDistance or Ant.bestPathDistance < 0:
          Ant.bestPathDistance = self.lastPathDistance
          Ant.bestPath = self.lastPath
        self.currentPathDistance = 0
        self.currentPath = []
        break

      self.currentPathDistance += graph.matrix[self.city][nextCity]
      self.city = nextCity
      self.currentPath.append(nextCity)

  def genPheromoneDepositMatrix(self, graph: Graph) -> Matrix:
    if (len(self.lastPath) <= graph.matrix.columns):
      return Matrix(graph.matrix.lines, graph.matrix.columns, -1)
    
    pheromoneMatrix: Matrix = Matrix(graph.matrix.lines, graph.matrix.columns, 0)
    pheromone: float = self.calcPheromoneToBeDeposited() #é o feromônio que vai ser depositado
    
    for i in range(len(self.lastPath) -1): #não quero chegar ao último item do array
      a, b = self.lastPath[i], self.lastPath[i + 1] #Maneira simples do python de fazer as várias atribuições
      pheromoneMatrix[a][b] = pheromoneMatrix[b][a] = pheromone
    
    return pheromoneMatrix
  
  def calcPheromoneToBeDeposited(self) -> float:
    if (self.lastPathDistance <= 0):
      return -1
    return 1/self.lastPathDistance