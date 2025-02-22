from entity.aco import Aco
import time

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
  aco: Aco = Aco("/home/joao/Documentos/GitHub/traveller_algorithm/assets/lau15_dist.txt", 0)
  # aco: Aco = Aco("/home/joao/Documentos/GitHub/traveller_algorithm/assets/sgb128_dist.txt", 0)
  aco.startACO()
  print(aco.currentBestPath)
  print(aco.currentBestPathDistance)


if __name__ == "__main__":
  main()