#! /usr/bin/env python_version
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 mayilong <mayilong@mayilong.lan>
#
# Distributed under terms of the MIT license.

"""

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res_max = 0
        start = 0
        letter_set = set()
        for i in range(len(s)):
            if s[i] not in letter_set:
                letter_set.add(s[i])
                res_max = max(i-start+1, res_max)
            else:
                while s[start] != s[i]: 
                    letter_set.remove(s[start])
                    start += 1
                start += 1
        return res_max


if __name__ == "__main__":
    print("*"*80)
    s = 'aab'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
