from entity.aco import Aco
import time

PATH="/home/joao/Documentos/GitHub/traveller_algorithm/assets/lau15_dist.txt"
ITERATIONS = 20
ANT_NUMBER = 0
DECAY_RATE = 0.5

def registerTime(func):
  def wrapper(*args, **kwargs):
    startTime: float = time.perf_counter()
    result = func(*args, **kwargs)
    endTime: float = time.perf_counter()
    print(f"{func.__name__} executed in {endTime - startTime:.6f} seconds")
    return result
  return wrapper

@registerTime
def main():
  aco: Aco = Aco(PATH, ANT_NUMBER, DECAY_RATE, ITERATIONS)
  aco.startACO()
  print("STARTED ACO ALGORITHM \n")
  print("BEST ENCOUNTERED PATH: ", aco.currentBestPath, "")
  print("DISTANCE OF PATH:", aco.currentBestPathDistance, "\n")
  print("FINISHED ALGORITHM \n\n")


if __name__ == "__main__":
  main()