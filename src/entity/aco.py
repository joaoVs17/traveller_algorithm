from entity.graph import Graph
from entity.ant import Ant
from typing import List
from entity.matrix import Matrix

class Aco:
  def __init__(self, filePath: str):
    self.graph: Graph = Graph(filePath)
    self.ants: List[Ant] = []
    for i in range(self.graph.matrix.columns):
      self.ants.append(Ant(i))
    self.decayRate = 0.5
    self.currentBestPath: List[int] = []
    self.currentBestPathDistance: float = -1
    self.bestAnt: Ant

  def decayPheromone(self):
    for line in range(0,self.graph.scoreMatrix.lines):
      for col in range(0,self.graph.scoreMatrix.columns):
        self.graph.scoreMatrix[line][col] = (1 - self.decayRate) * self.graph.scoreMatrix[line][col]

  def layNewPheromone(self):
    for ant in self.ants:
      pheromoneMatrix: Matrix = ant.genPheromeneDepositMatrix(self.graph)
      for line in range(0,self.graph.scoreMatrix.lines):
        for col in range(0,self.graph.scoreMatrix.columns):
          self.graph.scoreMatrix[line][col] += pheromoneMatrix[line][col]
  
  def makeAntsTour(self) -> None:
    for ant in self.ants:
      ant.travel(self.graph)
    # self.decayPheromone()
    self.layNewPheromone()


  def getBestValues(self):
    for ant in self.ants:
      if ant.lastPathDistance < self.currentBestPathDistance or self.currentBestPathDistance < 0:
        self.currentBestPathDistance = ant.lastPathDistance
        self.currentBestPath = ant.lastPath

  def startACO(self) -> None:
    for i in range(0,2):
      self.makeAntsTour()
      self.getBestValues()
     