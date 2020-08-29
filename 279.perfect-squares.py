# 279. 完全平方数
# https://leetcode-cn.com/problems/perfect-squares/


""" 思路
    典型的动态规划问题, 由下到上的计算思路


    dp[0] = 0  无效
    dp[1] = 1
    dp[2] = min(sys.maxsize, dp[2 - 1 * 1] + 1) = 1
    dp[3] = min(sys.maxsize, dp[3 - 1 * 1] + 1) = 1
    dp[4] = min(sys.maxsize, dp[4 - 1 * 1] + 1), dp[4 - 2 * 2] + 1) = 1
    dp[5] = min(sys.maxsize, dp[5 - 1 * 1] + 1), dp[5 - 2 * 2] + 1) = 2
    dp[6] = ....

    还是那句话，当前问题要依赖于之前的子问题
"""


import sys
class Solution:
    def numSquares(self, n):
        if n < 0:
            return -1
        dp = [sys.maxsize for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i - j * j] + 1, dp[i])
                j += 1
        return dp[n]


# # 这个版本有bug， 不过还是能通过leetcode
# class Solution:
#     def numSquares(self, n):
#         if n < 0:
#             return -1
#         dp = [sys.maxsize for i in range(n + 1)]
#         dp[0] = 0
#         # 因为这里没有判断n是不是大于1, 所以直接对dp[1]进行赋值会导致下表越界
#         dp[1] = 1
#         for i in range(1, n + 1):
#             j = 1
#             while j * j <= i:
#                 dp[i] = min(dp[i - j * j] + 1, dp[i])
#                 j += 1
#         return dp[n]


# class Solution:
#     def numSquares(self, n):
#         import math
#         import sys
#         if n < 0:
#             return -1
#         dp = [sys.maxsize for i in range(n + 1)]
#         dp[0] = 0
#         for i in range(1, n + 1):
#             # 这种写法不需要一次一次的计算平方值
#             for j in range(1, int(math.sqrt(i))+ 1):
#                 dp[i] = min(dp[i - j * j] + 1, dp[i])
#         return dp[n]


""" 思路
    这种是使用队列模拟BFS搜索的过程
                 12 
        3        8      11 
    1    2
0      
"""

# from collections import deque
# import math
# class Solution:
#     def numSquares(self, n):
#         if n <= 0:
#             return -1
#         q = deque()
#         q.append((n, 0))
#         while len(q):
#             tmp_node = q.popleft()
#             value, level = tmp_node
#             for j in range(int(math.sqrt(value)), -1, -1):
#                 if value - j * j > 0:
#                     q.append((value - j * j, level + 1))
#                 if value - j * j == 0:
#                     return level + 1


### timeout版本, 没办法使用备忘录递归
# import math
# class Solution:
#     count = 0
#     mem = dict()
#
#     def numSquares(self, n):
#         self.count = n
#         if n <= 0:
#             return 0
#         if n == 1:
#             return 1
#         self.helper(n, 0)
#         return self.count
#
#     def helper(self, n, depth):
#         if n < 0:
#             return
#         if n == 0:
#             self.count = min(self.count, depth)
#             return
#
#         for i in range(int(math.sqrt(n)), 0, -1):
#             if i * i <= n:
#                 self.helper(n - i * i, depth + 1)


import math
class Solution:
    mem = dict()

    def numSquares(self, n):
        for i in range(n+1):
            self.mem[i] = i

        res = self.helper(n)
        return res

    def helper(self, n):
        if self.mem[n] != n:
            return self.mem[n]

        if n == 0:
            return 0

        for i in range(int(math.sqrt(n)), 0, -1):
            if i * i <= n:
                self.mem[n] = min(self.mem[n], self.helper(n - i * i) + 1)
        return self.mem[n]


if __name__ == '__main__':
    sol = Solution()
    res = sol.numSquares(43)
    print(res)
