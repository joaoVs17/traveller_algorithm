from entity.graph import Graph
from entity.ant import Ant
from typing import List
from entity.npmatrix import Matrix
import multiprocessing as mp
import random

class Aco:
  def __init__(self, filePath: str, ants: int = 0, decayRate = 0.5, iterations: int = 1):
    self.graph: Graph = Graph(filePath)
    self.ants: List[Ant] = []

    if ants <= 0 or ants >= self.graph.matrix.columns: 
      ants = self.graph.matrix.columns-1
    for i in range(ants):
      self.ants.append(Ant(random.randint(0, self.graph.matrix.columns-1)))
    
    self.decayRate = decayRate if (decayRate < 1 and decayRate > 0) else 0.5
    self.iterations = iterations if iterations > 0 else 1
    self.currentBestPath: List[int] = []
    self.currentBestPathDistance: float = -1
    self.bestAnt: Ant

  def decayPheromone(self):
    self.graph.scoreMatrix *= (1 - self.decayRate)

  def layNewPheromone(self):
    for ant in self.ants:
      pheromoneMatrix: Matrix = ant.genPheromoneDepositMatrix(self.graph)
      self.graph.scoreMatrix += pheromoneMatrix

  def makeAntsTour(self) -> None:
    with mp.Pool(4) as pool:
      self.ants = pool.map(self.travelSingleAnt, self.ants)
        
    self.currentBestPath = Ant.bestPath
    self.currentBestPathDistance = Ant.bestPathDistance

    self.decayPheromone()
    self.layNewPheromone()

    for ant in self.ants:
      ant.city = random.randint(0, self.graph.matrix.columns-1)

  def travelSingleAnt(self, ant: Ant) -> Ant:
    ant.travel(self.graph)
    return ant

  def getBestValues(self):
    for ant in self.ants:
      if ant.lastPathDistance < self.currentBestPathDistance or self.currentBestPathDistance < 0:
        self.currentBestPathDistance = ant.lastPathDistance
        self.currentBestPath = ant.lastPath

  def startACO(self) -> None:
    for i in range(0, 1):
      self.makeAntsTour()
      self.getBestValues()
     