# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

"""

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""

""" 思路
    用一个临时的list记录下到目前为止最长的无重复子串，
        1。 如果新来的字符B已经在临时list
            （假设和B相等的字符在临时list中是A）， 需要从临时list的头部开始删除，一直删除到A,并且包括A
            将新来的元素B添加到临时list中
        2。 如果不在临时list中，直接添加到临时list中，更新最大长度
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        tmp_list = list()
        res = 0
        for i in range(len(s)):
            if s[i] in tmp_list:
                length = len(s) - 1
                while length >= 0 and len(tmp_list) > 0:
                    val = tmp_list.pop(0)
                    if val == s[i]:
                        break
                    length -= 1
            tmp_list.append(s[i])
            res = max(len(tmp_list), res)
        return res
