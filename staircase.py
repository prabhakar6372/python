#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
     x = ' '
     b = (n-1) - i
     a = str((x*b))
     d = str(((i+1)*'#'))
     print(a + d)
if __name__ == '__main__':
    n = int(input())
    staircase(n)
