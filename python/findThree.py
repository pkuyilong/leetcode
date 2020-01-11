# -*- coding: utf-8 -*-
# 2018-12-08 11:52 mayilong

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from torchvision import models


def test(nums):
    start, end = 0, len(nums) - 1
    if end < start:
        return -1
    while start < end:
        mid = (start + end)//2
        if nums[mid] ==3 :
            if mid > 0 and nums[mid-1] == 3:
                end = mid -1
            else:
                return mid
        elif nums[mid] < 3:
            start = mid + 1
        else:
            end = mid -1
    return -1




    pass

if __name__ == "__main__":
    print('*'*80)
    nums = [1,2,3,3,3,3,4,5,6]

    print(test(nums))

    pass
