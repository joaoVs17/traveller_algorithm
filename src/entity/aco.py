from entity.graph import Graph
from entity.ant import Ant
from typing import List
from entity.matrix import Matrix

class Aco:
  def __init__(self, filePath: str):
    self.graph: Graph = Graph(filePath)
    self.ants: List[Ant] = []
    self.ants.append(Ant(0))
    self.decayRate = 0.5

  def decayPheromone(self):
    for line in range(0,self.graph.scoreMatrix.lines):
      for col in range(0,self.graph.scoreMatrix.columns):
        self.graph.scoreMatrix[line][col] = (1 - self.decayRate) * self.graph.scoreMatrix[line][col]

