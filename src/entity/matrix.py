from typing import List, TypeVar
from io import TextIOWrapper
import re

class Matrix():
  def __init__(self, lines: int = 0, columns: int = 0, initialValue: float = 1) -> None :
    self._value: List[List[float]] = self.initialize(lines, columns, initialValue)
    self.lines: int = lines
    self.columns: int = columns

  @property
  def value(self) -> List[List[float]]:
    return self._value
  
  @classmethod
  def fromFile(cls, filePath: str) -> 'Matrix':
    lines: List[List[str]] = []
    with open(filePath, 'r') as file:
      for line in file:
        if '#' not in line:
          cost_list: List[str] = re.split(r'\s+', line.strip())
          lines.append(cost_list)

    matrix = cls(len(lines), len(lines[0]))
    # print(lines)
    for l in range (0, matrix.lines):
      for c in range (0, matrix.columns):
        matrix[c][l] = float(lines[l][c])
    return matrix
  
  def __repr__(self) -> str:
    return '\n'.join(['\t'.join(map(str, row)) for row in self.value])
  
  def __getitem__(self, index) -> List[float]:
    return self._value[index]

  def __setitem__(self, index, value) -> None:
    self._value[index] = value
  
  @classmethod
  def initialize(cls, lines: int = 0, columns: int = 0, fill: float = 0) -> List[List[float]]:
    return [[fill for _ in range(columns)] for _ in range(lines)]
  
  def fill(self, filePath: str) -> None:
    """Must fill the matriz based on a adjacence matrix"""
    pass
  