from abc import ABC, abstractmethod
from entity.npmatrix import Matrix
import numpy as np
class Graph: 
  def __init__(self, filePath: str) -> None:
    self.matrix: Matrix = Matrix.fromFile(filePath)
    self.scoreMatrix: Matrix = self.generateScoreMatrix(self.matrix)

  def generateMatrix(self, filePath: str) -> Matrix:
    return Matrix()
  
  def generateScoreMatrix(self, matrix: Matrix) -> Matrix:
    maxDistance = np.max(matrix._value)
    if maxDistance == 0:
      return Matrix(matrix.lines, matrix.columns, 0)
    score: float = 1 / (matrix.lines * maxDistance)  
    return Matrix(matrix.lines, matrix.columns, score)  

  
  

