# -*- coding: utf-8 -*-
# 2018-11-27 11:00 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from torchvision import models



class Solution(object):
    def validateStackSequences(self, pushed, popped):
        idx = 0
        stk = []
        for num in pushed:
            stk.append(num)
            while stk and stk[-1] == popped[idx]:
                idx += 1
                stk.pop()
        return not stk

if __name__ == "__main__":
    print('*'*80)
    pushed  = [1,2,3,4,5,6]
    popped =  []
    sol = Solution()
    print(sol.validateStackSequences(pushed, popped))
    pass
