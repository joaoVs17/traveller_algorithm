from typing import List
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

    matrix = cls(len(lines), len(lines[0])) #não tenho certeza ainda de como tipar isso
    
    for line in range (matrix.lines):
      for col in range (matrix.columns):
        matrix[col][line] = float(lines[line][col])
    
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
  