# 62. 不同路径
# https://leetcode-cn.com/problems/unique-paths/


class Solution_0:
    def uniquePaths(self, m, n):
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for item in dp:
            print(item)
        return dp[m-1][n-1]


class Solution:
    def uniquePaths(self, m, n):
        dp = [1 for i in range(n)]
        for i in range(1, m):
            dp[0] = 1
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[n-1]


if __name__ == '__main__':
    sol = Solution()
    res = sol.uniquePaths(4, 5)
    print(res)

