# -*- coding: utf-8 -*-
# 2018-12-07 17:37 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from torchvision import models


def test(nums):
    if nums is None or len(nums) == 0:
        return 0
    counts = [1]* len(nums)
    for i in range(1, len(nums)):
        max_tmp = 0 
        for j in range(0, i):
            if nums[j] < nums[i]:
                max_tmp = max(counts[i], counts[j])
        counts[i] = max_tmp + 1
    print(counts)
    return max(counts)


if __name__ == "__main__":
    print('*'*80)
    nums = [7,2,4,10,11,3,6,17,12]
    print(test(nums))
