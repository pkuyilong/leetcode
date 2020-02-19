# 343. 整数拆分
# https://leetcode-cn.com/problems/integer-break/

""" 思路
    典型的动态规划题目，需要做的就是找出dp[新的数字]和dp[老的数字]之间的关系
    因此
        直接看代码  0, 1, 2, 3, 4, 5, 6
           dp[0] = 0, 0, 1, 2, 4, 6, 9
    之后新来的数字
        dp[i] = max(dp[j] * (i - j))     3 < j < i
        为什么j是从3 而不是 从1呢?
        因为3之前的数字 0 ：0
                      1： 0 + 1   1 * 0 = 0
                      2: 1 + 1    1 * 1 = 1
                      3: 1 + 2    1 * 2 = 2
                      都带着一个1， 会导致dp[i]最终的结果不是最大的
              比如dp[5] = dp[3] * (5 - 2) = 1 * 2 * 2 = 4 不如 2 * 3 = 6 大
                      4: 2+ 2     2 * 2 = 4

    一开始我以为要将一个整数切分成n端，然后求这些数字的乘积的最大值，
    如果是这样的话，可以直接使用DFS+剪枝进行遍历，然后不断地计算它们的乘积
    最后获得最大值。
    比如8 可以拆分成3段的话， 可以[1, 2, 5], [1, 1, 6], [1, 3, 4], [2, 2, 3]
                    分别对应的max 为 10      6          12         12

    但是该题目没有要求一定要分成n段，因此n就是随机数字，使用DFS+剪枝遍历所有结果的话
    会耗费大量的时间，不可取

"""


class Solution:
    def integerBreak(self, n):
        d = {0: 0, 1: 0, 2: 1, 3: 2, 4: 4, 5: 6, 6: 9}
        if n < 7:
            return d[n]

        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        dp[6] = 9
        for i in range(7, n + 1):
            tmp_max = 0
            j = i - 1
            while j > 3:
                tmp_max = max(dp[j] * (i - j), tmp_max)
                j -= 1
            dp[i] = tmp_max
        return dp[n]


if __name__ == '__main__':
    res = Solution().integerBreak(8)
    print(res)
