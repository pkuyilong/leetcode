# -*- coding: utf-8 -*-
# 2018-12-07 17:49 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from torchvision import models

def test():


    pass

def binarySearch(nums, key, start, end):
    while start <= end:
        mid = (start + end)//2
        print(mid)
        if nums[mid] == key:
            return mid
        elif  key > nums[mid]:
            start = mid + 1
            print(start)
        else:
            end = mid - 1
    return -1


if __name__ == "__main__":
    print('*'*80)
    l = [2 ]
    print(binarySearch(l, 2, 0, 0))

