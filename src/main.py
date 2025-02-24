from entity.aco import Aco
import time
from pathlib import Path
from typing import List, Tuple


# FILENAME = "lau15_dist.txt"
# FILENAME = "fri26_d.txt"
FILENAME = "dantzig42_d.txt"
# FILENAME = "att48_d.txt"

ITERATIONS: int = 10
ANT_NUMBER: int = 21
DECAY_RATE: float = 0.5
SHOW_EACH_ITERATION_TIME: bool = True
PHEROMONE_INFLUENCE: float = 1
VISIBILITY_INFLUENCE: float = 2

def counter(func):  
  def wrapper(*args, **kwargs):
    startTime: float = time.perf_counter()
    result = func(*args, **kwargs)
    endTime: float = time.perf_counter()
    print(f"{func.__name__} executed in {endTime - startTime:.6f} seconds")
    return result
  return wrapper

@counter
def main() -> Tuple[List[int], float]:
  base_dir = Path(__file__).parent.parent
  path  = base_dir / "assets" / FILENAME
  aco: Aco = Aco(f"{path}", ANT_NUMBER, DECAY_RATE, ITERATIONS, PHEROMONE_INFLUENCE, VISIBILITY_INFLUENCE)
  print(f"STARTED ACO ALGORITHM - {len(aco.ants)} Ants // {aco.iterations} Iterations\n")
  aco.startACO(SHOW_EACH_ITERATION_TIME)
  print("BEST ENCOUNTERED PATH: ", aco.currentBestPath, "")
  print("DISTANCE OF PATH:", aco.currentBestPathDistance, "\n")
  print("FINISHED ALGORITHM \n\n")
  return aco.currentBestPath, aco.currentBestPathDistance

# @counter
# def using_main():
#   resultsDict: dict[float, int] = {}
#   for i in range(100):
#     bestP, dist = main()
#     if dist not in resultsDict:
#       resultsDict[float(dist)] = 1
#     else:
#       resultsDict[float(dist)] += 1
#   print(resultsDict.items())

if __name__ == "__main__":
  main()