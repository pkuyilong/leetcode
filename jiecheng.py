# -*- coding: utf-8 -*-
# 2018-11-18 11:30 mayilong 

import os
import sys
import numpy as np

# l = [0 for i in range(n+1)]
def jiecheng(n):
    if n== 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return  jiecheng(n-1)*n

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print('*'*80)
    # print(jiecheng(5))
    print(fib(4))
    pass

