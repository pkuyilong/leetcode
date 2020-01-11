# -*- coding: utf-8 -*-
# 2018-11-17 17:15 mayilong 

import os
import sys
import numpy as np

def sw(nums, k):
    # check boundary
    i = 0
    j = k-1
    tmp_i =0 
    cur = 0
    res = 0
    while tmp_i <= j:
        cur += nums[tmp_i]
        tmp_i += 1
    res = cur

    print(res)
    while j < len(nums)-1:
        i += 1
        j += 1
        cur = cur + nums[j] - nums[i-1]
        res = max(res, cur)
    return res

def sw2(nums):
    # find several numbers 


if __name__ == "__main__":
    print('*'*80)
    nums = [4,2,8,13,9,3,-1, 7, 15, 13]
    print(sw(nums, 4))
    pass
