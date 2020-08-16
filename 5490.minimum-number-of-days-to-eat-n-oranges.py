# https://leetcode-cn.com/problems/minimum-number-of-days-to-eat-n-oranges/

"""
这道题主要是记忆化递归的题目, 也可以看作是动态规划的题目
"""

class Solution(object):
    mem = {}

    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 2

        if n in self.mem:
            return self.mem[n]
        res = min(self.minDays(n // 2) + n % 2, self.minDays(n // 3) + n % 3) + 1
        self.mem[n] = res
        return res


"""
我当时的做法, 如果苹果数量特别大, 那么需要申请一个很大的数组, 而且依次遍历, 把该数组填满,会很浪费时间
"""

# class Solution(object):
#     def minDays(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n <= 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n == 3:
#             return 2
#
#         dp = [0 for i in range(n + 1)]
#         dp[1] = 1
#         dp[2] = 2
#         dp[3] = 2
#
#         for i in range(4, n + 1):
#             if i % 2 == 0 and i % 3 == 0:
#                 dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3]) + 1
#             elif i % 2 == 0:
#                 dp[i] = min(dp[i - 1], dp[i // 2]) + 1
#             elif i % 3 == 0:
#                 dp[i] = min(dp[i - 1], dp[i // 3]) + 1
#             else:
#                 dp[i] = dp[i - 1] + 1
#         # print(dp)
#         return dp[n]
