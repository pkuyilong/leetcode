# 121. 买卖股票的最佳时机
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""思路
    将每一天的价格减去前一天的价格，得到一个数列
    将问题转换成计算最大子序列，计算这个数列中的最大子序列就是最低价买入和最高价卖出的价差

"""


class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) == 0:
            return 0
        if len(prices) < 2:
            return 0

        diff = []
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i - 1])
        # print(diff)

        # 这一部分是求最大子序列的代码
        dp = [0 for i in range(len(diff))]
        dp[0] = diff[0]
        max_res = diff[0]
        for i in range(1, len(diff)):
            dp[i] = max(dp[i - 1], 0) + diff[i]
            max_res = max(max_res, dp[i])
        print(dp)
        return max_res if max_res > 0 else 0


if __name__ == '__main__':
    prices = [1, 2, 4]
    res = Solution().maxProfit(prices)
    print(res)