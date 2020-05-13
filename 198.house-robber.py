# 198. 打家劫舍
# https://leetcode-cn.com/problems/house-robber/


""" 思路
    dp[i]表示到第i个位置，偷到的最大数量
    在第i个位置，有两种选择：
        1. 偷
        2. 不偷
    dp[i] = max( dp[i-2] + nums[i], 偷了第i个位置
                 dp[i-1]            没偷第i个位置
                )

"""


class Solution_0:
    def rob(self, nums):
        if not nums or len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        print(dp)
        return dp[len(nums)-1]


class Solution():
    def rob(self, nums):
        pre, cur = 0, 0
        for num in nums:
            tmp_cur = cur
            cur = max(pre + num, cur)
            pre = tmp_cur
            # cur, pre = max(pre + num, cur), cur
            print(cur)
        return cur


if __name__ == '__main__':
    nums = [2, 3, 2, 2, 3]
    print(nums)
    res = Solution().rob(nums)
    print(res)
