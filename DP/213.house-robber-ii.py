# 213. 打家劫舍 II
# https://leetcode-cn.com/problems/house-robber-ii/

"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
"""

""" 思路
    本题与之前的198题基本相似，不同的在于加了一个限制条件
    对于第一个和最后一个房子，不能同时偷，!第一个 and !最后一个
    所以对这个条件取反，就是
        1. 偷第一个房子，不偷最后的房子
        2. 偷最后一个房子，不偷第一个房子
        3. 两个房子都不偷
        
    这个问题有点类似于背包问题，对于每一个位置都有偷或者不偷两种选择，
    之后在不偷第一个房子 和 不偷最后一个房子 两种情况中去最大值即可
    两个房子都不偷的情况其实都包括在1 和 2 中。

"""


class Solution(object):
    def rob(self, nums):
        if not nums or len(nums) == 0:
            return 0
        if len(nums) < 2:
            return nums[0]
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))

    def rob_helper(self, nums):
        pre, cur = 0, 0
        for num in nums:
            origin_cur = cur
            cur = max(pre + num, cur)
            pre = origin_cur
        return cur


if __name__ == '__main__':
    nums = [2, 3, 2]
    res = Solution().rob(nums)
    print(res)
