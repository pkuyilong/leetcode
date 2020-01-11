# -*- coding: utf-8 -*-
# 2018-11-04 18:48 mayilong 

import os
import sys
import numpy as np

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        idx = 0
        for item in nums:
            if item != nums[idx]:
                idx += 1
                nums[idx] = item
                print(nums)
        return idx + 1

    def removeDuplicates2(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        s = set()
        for item in nums:
            s.add(item)
        return len(s)


if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,1,2,4,5,5,6,6,6,]
    res = sol.removeDuplicates2(nums)
    print(res)
    pass
