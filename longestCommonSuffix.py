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
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        letter_idx = 0
        if len(strs) == 1:
            return strs[0]
        sLen = len(strs[0])
        for s in strs:
            sLen = min(sLen, len(s))
        letter_idx = 0
        for i in range(sLen):
            for str_idx in range(1, len(strs)):
                if strs[str_idx][letter_idx] != strs[str_idx-1][letter_idx]:
                    return strs[0][:letter_idx]
                else:
                    pass
            letter_idx += 1
        return strs[0][:letter_idx] 

if __name__ == "__main__":
    print("*"*80)
    sol = Solution()
    strs = ['flower', 'flight', 'flow']
    res = sol.longestCommonPrefix(strs)
    print(f"res is {res}")
    print(type(res))
    
