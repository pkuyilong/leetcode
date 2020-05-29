# 198. 打家劫舍
# https://leetcode-cn.com/problems/house-robber/


""" 思路
    1.简单情况：
        如果只有一个房子， 肯定要偷。
        如果有两个房子，肯定要偷财产多的
        如果有三个房子呢？ A B C三个房子
            此时会有两种选择，一种是偷A和C， 另一种是偷B
            如果A + B greater than B, 要选择偷AC，否则偷B
            也就是说，C位置的时候，考虑是A+C大呢还是B大的问题。 OK？
            即dp[C] = max(dp[A] + nums[c], dp[B])
    假设dp[i]代表到当前位置i的时候做出的最优的选择，
    那么
        dp[i] = max(dp[i-2] + nums[c], dp[i-1]

    2.直接考虑也行：
    dp[i]表示到第i个位置，偷到的最大数量
    在第i个位置，有两种选择：
        1. 偷
        2. 不偷
    dp[i] = max( dp[i-2] + nums[i], 偷了第i个位置, 要想最大话，肯定也要偷之前位置，但是不能是相邻的位置
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
