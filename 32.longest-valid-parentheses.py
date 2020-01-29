# 32. 最长有效括号
# https://leetcode-cn.com/problems/longest-valid-parentheses/

from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        stk = deque()
        last = -1
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                # 放入的是下表
                stk.append(i)
            else:
                if len(stk):
                    tmp = stk.pop()
                    if tmp == last + 2:
                        res = res + i - tmp + 1
                    else:
                        res = max(res, i - tmp + 1)
                    last = tmp
                else:
                    continue
        print(res)
        return res

class Solution_1:
    def longestValidParentheses(self, s: str) -> int:
        """ 思路
            1.
            2.
            3. 及时更新最大值
        """
        if s is None or len(s) == 0:
            return 0
        dp = [0 for i in range(len(s))]
        res = 0
        stk = deque()
        if s[0] == '(':
            stk.append(s[0])
        for i in range(1, len(s)):
            if s[i] == '(':
                stk.append(s[i])
                dp[i] = dp[i-1]
            else:
                if len(stk):
                    stk.pop()
                    dp[i] = dp[i-1] + 2
                    res = max(res, dp[i])
                else:
                    dp[i] = 0
        print(dp)
        return res


if __name__ == '__main__':
    s = "()(())"
    sol = Solution()
    res = sol.longestValidParentheses(s)
    print(res)




