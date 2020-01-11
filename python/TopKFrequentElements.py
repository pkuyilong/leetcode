# -*- coding: utf-8 -*-
# 2018-11-24 13:58 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        res = []
        d = defaultdict(int)
        # d = dict()
        # for num in nums:
        #     if num not in d.keys():
        #         d[num] = 1
        #     else:
        #         d[num] = d[num] + 1
        for num in nums:
            d[num] = d[num] + 1
        another_d = dict(sorted(d.items(), key=lambda x:x[1],reverse=True))
        cnt = 0
        for num, num_count in another_d.items():
            if cnt < k:
                res.append(num)
                cnt += 1
        return res



def test():
    pass

if __name__ == "__main__":
    # l = [1,1,1,2,2,3]
    l = [4,1,-1,2,-1,2,3]
    sol = Solution()
    print(sol.topKFrequent(l, 2))
    print('*'*80)
    test()
    pass
