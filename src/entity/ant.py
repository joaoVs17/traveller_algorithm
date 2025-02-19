from typing import List
from entity.graph import Graph
import random

class Ant:
  id = 0
  def __init__(self, city: int):
    self.city: int = city
    self.travelling: bool = False
    self.last_path: List[int] = []
    self.currentPath: List[int] = []

  def calcTravelProbability(self, cityA: int, cityB: int, graph: Graph, feromoneInfluence: float, visibilityInfluence: float):
    edgeFeromone: float = graph.scoreMatrix[cityA][cityB]
    edgeVisibility: float = 1/graph.matrix[cityA][cityB] if graph.matrix[cityA][cityB] != 0 else 0

    divider: float = 0
    for col in range (graph.matrix.columns):
      if (col not in self.currentPath) and (col != cityA) :
        secondaryEdgeFeromone: float = graph.scoreMatrix[cityA][col]
        secondaryEdgeVisibility: float = 1/graph.matrix[cityA][col] if graph.matrix[cityA][col] != 0 else 0
        divider += pow(secondaryEdgeFeromone, feromoneInfluence) * pow(secondaryEdgeVisibility, visibilityInfluence)
    dividend: float = pow(edgeFeromone, feromoneInfluence) * pow(edgeVisibility, visibilityInfluence)

    if (divider == 0): 
      return 0
    
    probability: float = dividend/divider
    return probability

  def pickNextCity(self, graph: Graph, currentCity: int) -> int:
    
    probabilityObj: dict[int, float]  = {}
    maxProbability: float = 0
    
    for city in range(graph.matrix.columns):
      if (city not in self.currentPath) and (city != currentCity):
        probability: float = self.calcTravelProbability(currentCity, city, graph, 1, 2)
        probabilityObj[city] = probability
        maxProbability = max(maxProbability, probability)
    
    if not list(probabilityObj.keys()):
      return -1
    
    while True:
      #Ideia: usar as probabilidades como teto de aceitação. Um número é randomizado e, caso esteja dentro desse teto é escolhido
      #Números maiores possuem, portanto, maior chance de serem escolhidos
      chosenCity: int = random.choice(list(probabilityObj.keys()))
      acceptance: float = probabilityObj[chosenCity] / maxProbability
      if random.random() <= acceptance:
        return chosenCity
  
  def travel(self, graph: Graph) -> None:
    self.currentPath.append(self.city)
    while True:
      self.travelling = True
      nextCity = self.pickNextCity(graph, self.city)
      if (nextCity < 0):
        self.city = self.currentPath[0]
        self.last_path = self.currentPath
        self.currentPath = []
        break
      self.city = nextCity
      self.currentPath.append(nextCity)


      
    
