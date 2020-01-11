# -*- coding: utf-8 -*-
# 2018-11-04 22:49 mayilong 

import os
import sys
import numpy as np


def partition(nums, start, end):
    if start >= end:
        return 0
    i, j = start , end
    key = nums[start]
    while i < j:
        while i < j and nums[j] > key:
            j -= 1
        while i < j and nums[i] < key:
            i += 1
        print(i, j)
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            nums[i], key = key, nums[i]
    print(nums)
    return i + 1

if __name__ == "__main__":
    print('*'*80)
    nums = [5, 17, 12, 28, 5, 13, 11]
    # nums = [5, 17]
    res = partition(nums, 0, len(nums) -1)
    print(res)
    pass
