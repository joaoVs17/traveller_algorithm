from abc import ABC, abstractmethod
from entity.matrix import Matrix
class Graph: 
  def __init__(self, filePath: str) -> None:
    self.matrix: Matrix = Matrix.fromFile(filePath)
    self.scoreMatrix: Matrix = self.generateScoreMatrix(self.matrix)

  def generateMatrix(self, filePath: str) -> Matrix:
    return Matrix()
  
  def generateScoreMatrix(self, matrix: Matrix) -> Matrix:
    maxDistance = matrix[0][0]
    for line in range(0, matrix.lines):
      for col in range(0, matrix.columns):
        if matrix[line][col] > maxDistance:
          maxDistance: float = matrix[line][col]  
    return Matrix(matrix.lines, matrix.columns, 1/(matrix.lines*maxDistance))
  
  

