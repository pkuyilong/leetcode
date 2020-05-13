# 70. 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        dp = [0 for i in range(n+1)]
        if n <= 2:
           return 1 if n == 1 else 2
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
