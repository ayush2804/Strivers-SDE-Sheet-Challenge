from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]):
	# Write your code here.
    col = set()
    row = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in range(len(matrix)):
        for j in col:
            matrix[i][j] = 0
    for i in range(len(matrix[0])):
        for j in row:
            matrix[j][i] = 0
    
