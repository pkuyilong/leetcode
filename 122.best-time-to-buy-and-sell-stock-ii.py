# 122. 买卖股票的最佳时机 II
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/


"""思路
    不同于题目121，这道题目强调可以多次买卖，也就是有利益差就可以执行交易
    但是这道题并不关系你如何交易，只需要知道最大的利益就可以
    prices = [7, 1, 5, 3, 6, 4]
    首先计算出相邻两天价格的价差
    diff   =     -6， 4， -2， 3， -2
    所以只需要关注大于0的数值就可以，正数可以代表盈利



    可能有人会有这样的疑问 因为题目规定了不可以同时开始多笔交易
    prices = [1, 4, 7, 8, 5, 2]
    首先计算出相邻两天价格的价差
    diff   =    3, 3, 1, -3, -3
    为了得到第一个3，要在第一天买入，第二天卖出，但是因为条件限制，卖出的当天不可以买进股票
    所以第二个3是怎么得到的呢？
    其实你可以在第一天买入，第二天不卖出，第三天不卖出，知道第四天才卖出就可以顺利的赚到
    3 + 3 + 1 = 8 - 1
    所以只需要关注大于0的数值就可以，正数可以代表盈利

"""


# class Solution:
#     def maxProfit(self, prices):
#         if not prices or len(prices) == 0:
#             return 0
#         total = 0
#         diff = []
#         for i in range(1, len(prices)):
#             diff.append(prices[i] - prices[i - 1])
#         for di in diff:
#             if di > 0:
#                 total += di
#         return total


class Solution:
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0

        vally = prices[0]
        peak = prices[0]
        res = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            vally = prices[i]
            print("vally is {}".format(vally))
            i += 1

            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            print("peak is {}".format(peak))
            res = res + peak - vally
        return res


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    res = Solution().maxProfit(prices)
    print(res)
