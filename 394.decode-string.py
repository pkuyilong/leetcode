# 394. 字符串解码
# https://leetcode-cn.com/problems/decode-string/

"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import deque


class Solution_0(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = list()
        res = ""
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                res += c
            elif c == '[':
                stk.append((res, num))
                res = ""
                num = 0
            elif c == ']':
                last_str, count = stk.pop()
                res = last_str + count * res
        return res



class Solution(object):
    i = 0
    def decodeString(self, s):
        num = 0
        if len(s) < 1:
            return ""

        res = ""
        while self.i < len(s):
            if s[self.i].isdigit():
                while self.i < len(s) and s[self.i].isdigit():
                    num = num * 10 + int(s[self.i])
                    self.i += 1
            elif s[self.i] == '[':
                self.i += 1
                word = self.decodeString(s)
                while num > 0:
                    num -= 1
                    res += word
            elif s[self.i] == ']':
                self.i += 1
                return res
            else:
                res += s[self.i]
                self.i += 1
        return res


if __name__ == '__main__':
    s = "3[a]2[bc]"
    sol = Solution()
    res = sol.decodeString(s)
    print(res)
