# -*- coding: utf-8 -*-
# 2018-11-04 19:22 mayilong 

import os
import sys
import numpy as np


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None and len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        count = 0
        idx = 0
        for item in nums:
            count += 1
            if item == nums[idx]:
                if count <= 2:
                    nums[idx] = item
                    idx += 1
                else:
                    count = 0
            else:
                nums[idx] = item
                idx += 1
        print(nums)
        return idx



    def removeDuplicates2(self, nums):
        d = dict()
        for item in nums:
            d[item] = d.get(item, 0) + 1
        idx = 0
        for item in d.items():
            if item[1] ==1:
                nums[idx] = item[0]
                idx += 1
            else:
                nums[idx] = item[0]
                idx += 1
                nums[idx] = item[0] 
                idx += 1
        print(nums)



if __name__ == "__main__":
    nums = [1,1,1,2,3,4,4,4,5,6]
    sol = Solution()
    res = sol.removeDuplicates(nums)
    print(res)


    pass
