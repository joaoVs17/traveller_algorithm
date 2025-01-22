from abc import ABC, abstractmethod
from typing import List, TypeVar

T = TypeVar('T')
Matrix = List[List[T]]

class Matrix(ABC):
  def __init__(self, lines: int = 0, columns: int = 0) -> None :
    pass

class Graph: 
  def __init__(self, filePath: str) -> None:
    self.matrix: Matrix = self.generateMatrix(filePath)
    self.scoreMatrix: Matrix = self.generateScoreMatrix();

  def generateMatrix(self, filePath: str) -> Matrix:
    return Matrix()
  
  def generateScoreMatrix(self, lines: int = 0, columns: int = 0) -> Matrix:
    return Matrix()