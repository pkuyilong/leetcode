# 303. 区域和检索 - 数组不可变
# https://leetcode-cn.com/problems/range-sum-query-immutable/


"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

"""

""" 思路
            [-2, 0, 3, -5, 2, -1]
      dp [0, -2, -2, 1, -4, -2, -3]  
      dp 表示到当前位置，前边的所有数据（包括当前位置）的累加和
      假设要求[1,3]  == dp[4] - dp[1] = -4 - (-2) = -2 
"""


class NumArray(object):

    def __init__(self, nums):
        if not nums or len(nums) == 0:
            raise RuntimeError("nums is invalid")

        self.dp = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.dp[i + 1] = self.dp[i] + nums[i]

    def sumRange(self, i, j):
        if j < i:
            return 0
        return self.dp[j + 1] - self.dp[i]
