from entity.graph import Graph
from entity.ant import Ant
from typing import List
from entity.npmatrix import Matrix
import multiprocessing as mp
import random
import time

def counter(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("showTime", False):
            startTime = time.perf_counter()
            result = func(*args, **kwargs)  # Execute function
            endTime = time.perf_counter()
            print(f"{func.__name__} executed in {endTime - startTime:.6f} seconds")
            return result
        else:
            return func(*args, **kwargs)  # Ensure function runs even if showTime is False
    return wrapper

class Aco:
  def __init__(self, filePath: str, ants: int = 0, decayRate = 0.5, iterations: int = 1, pheromoneInfluence: float = 1, visibilityInfluence: float = 2):
    self.graph: Graph = Graph(filePath)
    self.ants: List[Ant] = []

    if ants <= 0 or ants >= self.graph.matrix.columns: 
      ants = self.graph.matrix.columns
    
    cities = list(range(self.graph.matrix.columns))
    random.shuffle(cities)
    self.ants = [Ant(cities[i], pheromoneInfluence, visibilityInfluence) for i in range(ants)]
    
    self.decayRate = decayRate if (decayRate < 1 and decayRate > 0) else 0.5
    self.iterations = iterations if iterations > 0 else 1
    self.pheromoneInfluence: float = pheromoneInfluence
    self.visibilityInfluence: float =  visibilityInfluence
    self.currentBestPath: List[int] = []
    self.currentBestPathDistance: float = -1
    self.bestAnt: Ant

  def decayPheromone(self):
    self.graph.scoreMatrix *= (1 - self.decayRate)

  def layNewPheromone(self):
    for ant in self.ants:
      pheromoneMatrix: Matrix = ant.genPheromoneDepositMatrix(self.graph)
      self.graph.scoreMatrix += pheromoneMatrix

  @counter
  def makeAntsTour(self, showTimes: bool = False) -> None:
    with mp.Pool(4) as pool:
      self.ants = pool.map(self.travelSingleAnt, self.ants)
        
    self.decayPheromone()
    self.layNewPheromone()

    cities = list(range(self.graph.matrix.columns))
    random.shuffle(cities)
    
    for i in range(len(self.ants)):
      self.ants[i].city = cities[i]

  def travelSingleAnt(self, ant: Ant) -> Ant:
    ant.travel(self.graph)
    return ant

  def getBestValues(self):
    for ant in self.ants:
      if ant.lastPathDistance < self.currentBestPathDistance or self.currentBestPathDistance < 0:
        self.currentBestPathDistance = ant.lastPathDistance
        self.currentBestPath = ant.lastPath

  def startACO(self, showTimes: bool = False, showPartialResults: bool = False) -> None:
    for i in range(0, self.iterations):
      self.makeAntsTour(showTimes=showTimes)
    self.getBestValues()
     