from abc import ABC, abstractmethod
from entity.matrix import Matrix
class Graph: 
  def __init__(self, filePath: str) -> None:
    self.matrix: Matrix = Matrix.fromFile(filePath)
    self.scoreMatrix: Matrix = Matrix(self.matrix.lines, self.matrix.columns)

  def generateMatrix(self, filePath: str) -> Matrix:
    return Matrix()
  
  def generateScoreMatrix(self, lines: int = 0, columns: int = 0) -> Matrix:
    return Matrix()
  

