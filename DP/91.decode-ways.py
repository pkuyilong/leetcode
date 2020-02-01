# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/

""" 思路
    这是个升级版本的爬楼梯，我一时间竟然没有反应过来，
    不过我想到了肯定是dp[i] 与 dp[i-1]、dp[i-2]有关系，
    然而并没有把其中的关系理清楚

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # 如果第一个字符就是'0'，那么肯定无法解析
        if not s or s[0] == '0':
            return 0

        # 从这里就不用考虑开头是'0'的情况了，可以将dp[1]置为1
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            # 首先处理字符为'0'的情况
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0

            else:
                if s[i - 1] == '1' or s[i - 1] == '2' and '0' < s[i] < '7':
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        # print(dp)
        return dp[len(s)]


if __name__ == '__main__':
    s = "10"
    res = Solution().numDecodings(s)
    print(res)
