# 322. 零钱兑换
# https://leetcode-cn.com/problems/coin-change/

"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。
"""

""" 思路
    coins = [1, 2, 5] amount = 10
    dp[i]代表凑成价值i源所需要的最小的硬币个数
    
    dp 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = min(dp[3-1]， dp[3-2]) + 1 = min(1, 1) + 1 = 2
    dp[4] = min(dp[4-1], dp[4-2]) + 1 = min(2, 1) + 1 = 2
    dp[5] = 1
    dp[6] = min(dp[6-1], dp[6-2], dp[6-5]) = min(1, 2, 1) + 1 = 2
    以6为例，当我们想凑齐6元所需要的最小硬币数的时候，我们可以依赖之前计算过的数值，
    因为之前的d[0] ~ d[5]都是最优解了，所以我们可以在之前的最优解上进一步的扩充
    
    要想求得一个大问题的最优解，那么要保证其中的子问题一定也是最优解
    
"""

import sys


class Solution():
    def coinChange(self, coins, amount):
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            cost = sys.maxsize
            for c in coins:
                if i - c >= 0:
                    # 犯了一个严重的错误，逻辑上应该找到dp[i-coin] + 1 的最小值
                    # 所以应该和 dp[i-c] + 1 作比较，不然如果cost一直比较小，
                    # 那么cost相当于在比较完成之后作了自加一操作  cnst = cost + 1
                    cost = min(cost, dp[i - c] + 1)
            dp[i] = cost

        if dp[amount] == sys.maxsize:
            return -1
        else:
            return dp[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 10
    res = Solution().coinChange(coins, amount)
    print(res)
