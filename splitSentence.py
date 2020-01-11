# -*- coding: utf-8 -*-
# 2018-11-04 21:27 mayilong 

import os
import sys
import numpy as np


class Solution():
    def splitSentence(self, s):
        l = list()
        l1 = list()
        idx = 0
        while idx < len(s):
            l1.clear()
            str = ''
            l1.clear()
            if s[idx].isalnum():
                while s[idx].isalnum():
                    l1.append(s[idx])
                    idx += 1
                l.append(str.join(l1))
            else:
                idx += 1
        print(" ".join(l))
        pass

    def splitSentence2(self, s):
        idx = 0
        l = [s[0]] 
        for i in range(len(s)):
            if s[i] != s[idx]:
                l.append(s[i])
                idx += 1
        print("".join(l))

if __name__ == "__main__":
    sol = Solution()
    sen = 'A man is    under the  tree  , well !'
    sol.splitSentence2(sen)
    s = ""
    l = ['h', 'e']
    print(s.join(l))
    # s = ',hello'
    # res = s.index('e', 0, 4)
    # print(res)
    # print(s[0].isalnum())

    pass
