from typing import List, Union
import re
import numpy as np

#Para usar o numpy houve uma certa negligência com a tipagem
class Matrix():
  def __init__(self, lines: int = 0, columns: int = 0, initialValue: float = 1) -> None :
    self._value = self.initialize(lines, columns, initialValue)
    self.lines: int = lines
    self.columns: int = columns

  @property
  def value(self):
    return self._value
  
  @classmethod
  def fromFile(cls, filePath: str) -> 'Matrix':
    lines: List[List[float]]= []
    with open(filePath, 'r') as file:
      for line in file:
        if '#' not in line:
          cost_list = re.split(r'\s+', line.strip())
          lines.append(list(map(float, cost_list)))

    numLines: int = len(lines)
    numColumns: int = len(lines[0]) if numLines > 0 else 0

    matrix = cls(numLines, numColumns)  
    matrix._value = np.array(lines, dtype=float)  #valor colocado diretamente (usado array do numpy)

    return matrix
  
  def __repr__(self) -> str:
      return '\n'.join(['\t'.join(map(str, row)) for row in self._value])

  def __getitem__(self, index: int) -> np.ndarray:
      return self._value[index]

  def __setitem__(self, index: int, value: Union[list, np.ndarray]) -> None:
      self._value[index] = value

  def __imul__(self, val: float) -> 'Matrix':
    self._value *= val
    return self
  
  def __add__(self, val: 'Matrix') -> 'Matrix':
    if self._value.shape != val._value.shape:
      raise ValueError("Para adição, as dimensões das matrizes devem ser iguais")
    result = Matrix(self.lines, self.columns)  
    result._value = self._value + val._value
    return result

  def __iadd__(self, val: 'Matrix') -> 'Matrix':
    if self._value.shape != val._value.shape:
      raise ValueError("Para adição, as dimensões das matrizes devem ser iguais")
    self._value += val._value
    return self

  @classmethod
  def initialize(cls, lines: int = 0, columns: int = 0, fill: float = 0):
    return np.full((lines, columns), fill, dtype=float)
  