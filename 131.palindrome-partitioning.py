# https://leetcode-cn.com/problems/palindrome-partitioning/

"""与93题 恢复ip地址思路一致"""

"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = list()
        if s == '':
            return ans
        tmp = list()
        self.helper(s, tmp, ans)
        return ans

    def helper(self, s, tmp, ans):
        if len(s) == 0:
            ans.append(tmp[:])
            return

        for i in range(len(s)):
            cur = s[:i + 1]
            if self.valid(cur):
                tmp.append(cur)
                self.helper(s[i + 1:], tmp, ans)
                tmp.pop()

    def valid(self, s):
        """
        注意right是闭区间，所以是len(s) - 1
        """
        left, right = 0, len(s) - 1
        # 注意 left == right 的情况下，没有参与到while循环中，但是中间那个元素不影响回文字符串的判别
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        tmp = list()
        ans = list()
        if s is None or len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]
        self.helper(s, tmp, ans)
        return ans

    def helper(self, s, tmp, ans):
        if len(s) == 0:
            ans.append(tmp[:])
            return

        for i in range(len(s)):
            front = s[:i + 1]
            end = s[i + 1:]
            if self.is_valid(front):
                tmp.append(front)
                self.helper(end, tmp, ans)
                tmp.pop()

    def is_valid(self, s):
        return s == s[::-1]