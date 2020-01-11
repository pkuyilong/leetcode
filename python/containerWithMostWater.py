# -*- coding: utf-8 -*-
# 2018-11-25 11:33 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from torchvision import models
class Solution:
    def maxArea(self, height):
        waters = 0
        res = 0
        for i in range(len(height) - 1):
            min_value = height[i]
            for j in range(i+1, len(height)):
                min_value = min(min_value, height[j])
                waters = min_value *(j-i+1)
                res = max(waters, res)
        return res

def test():
    pass

if __name__ == "__main__":
    print('*'*80)
    # height = [1,8,6,2,5,4,8,3,7]
    height =[2,1,5,6,2,3] 
    sol = Solution()
    print(sol.maxArea(height))
    # test()
    pass
