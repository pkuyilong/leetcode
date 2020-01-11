# -*- coding: utf-8 -*-
# 2018-11-26 10:23 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from torchvision import models
from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, A):
        d = defaultdict(int)
        for item in A:
            d[item] += 1
        another_d = defaultdict(int)
        for k,v in d.items():
            if v > 1:
                another_d[k] = v-1
        print(another_d)
        A_set = set(A) 
        cnt = 0
        for k,v in another_d.items():
            for i in range(v):
                while k in A_set:
                    k += 1
                    cnt += 1
                A_set.add(k)
        return cnt

def test():
    pass

if __name__ == "__main__":
    print('*'*80)
    # A = [3,2,1,2,1,7]
    A = [1,2,2]
    sol = Solution()
    print(sol.minIncrementForUnique(A))

    test()
    pass
