# https://leetcode-cn.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num2idx = dict()
        for idx, num in enumerate(nums):
            if target - num in num2idx.keys():
                return num2idx[target - num], idx
            num2idx[num] = idx


