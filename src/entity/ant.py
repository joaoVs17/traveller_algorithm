from typing import List
from entity.graph import Graph

class Ant:
  id = 0
  def __init__(self, city: int):
    self.city = city
    self.last_path: List[int] = []
    self.currentPath: set[int] = set()

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

