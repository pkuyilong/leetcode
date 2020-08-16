# https://leetcode-cn.com/problems/palindrome-partitioning-ii/


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0 or len(s) == 1:
            return 0
        dp = [i for i in range(len(s))]
        for i in range(1, len(s)):
            for j in range(i):
                if j == 0:
                    if self.is_valid(s[:i+1]):
                        dp[i] = 0
                        break
                else:
                    tmp = s[j: i+1]
                    if self.is_valid(tmp):
                        dp[i] = min(dp[j-1] + 1, dp[i])
                    else:
                        dp[i] = dp[i-1] + 1
        print(dp)
        return dp[len(s) - 1]


    def is_valid(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    s = 'abcccb'
    sol = Solution()
    ans = sol.minCut(s)
    print(ans)