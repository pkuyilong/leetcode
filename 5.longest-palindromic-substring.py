# https://leetcode-cn.com/problems/longest-palindromic-substring/

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
""" 方法1
class Solution(object):
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ""
        max_len = 0
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                res = self.check(s, i, j)
                print(i, j, res)
                if res:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        ans = s[i: j + 1]
        return ans

    def check(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
 """

""" 方法2 """


class Solution(object):
    def longestPalindrome(self, s):
        rev = s[::-1]
        res = self.longestPalindrome(s, rev)
        return res

    def longCommonSubstring(self, s, t):
        pass


if __name__ == '__main__':
    s = "cbbd"
    sol = Solution()
    res = sol.longestPalindrome(s)
    print(res)
