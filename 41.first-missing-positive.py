# https://leetcode-cn.com/problems/first-missing-positive/

"""
41. 缺失的第一个正数
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。



示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
"""

import sys


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n_set = set(nums)
        i = 1
        while i < sys.maxsize:
            if i not in n_set:
                return i
            i += 1
