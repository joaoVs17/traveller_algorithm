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
