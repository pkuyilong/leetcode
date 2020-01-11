# -*- coding: utf-8 -*-
# 2018-11-17 14:52 mayilong 

import os
import sys
import numpy as np
class Solution:
    # def lengthOfLongestSubstring(self, s):
        # if s is None and len(s) == 0:
            # return 0

        # letter_last_pos = dict()
        # origin_list = list(s)
        # letter_list = []
        # i, j = 0, 0
        # len_max = 0
        # cur = 0
        # while i <= j and j < len(s):

            # if s[j] not in letter_list:
                # letter_last_pos[s[j]] = j 
                # letter_list = origin_list[i:j+1]
                # cur = len(letter_list)
                # print('not in   {}'.format(letter_list))
            # else:
                # i = letter_last_pos[s[j]] + 1
                # del letter_list[:]
                # print("{}  {}".format(i, j))
                # letter_list = origin_list[i:j+1]
                # letter_last_pos[s[j]] = j 
                # cur = len(letter_list)
                # print('in   {}'.format(letter_list))
            # len_max = max(cur, len_max)
            # j += 1
        # return len_max

    def lengthOfLongestSubstring2(self, s):
        if s is None and len(s) == 0:
            return 0
        letter_set = set()
        i, j = 0, 0
        cur, res = 0, 0 
        while i <= j and j < len(s):
            if s[j] not in letter_set:
                letter_set.add(s[j])
                print(letter_set)
                cur = j - i +1
                res = max(cur, res)
                j += 1
            else:
                letter_set.remove(s[i])
                i += 1
        return res

def l2(s):
    n = len(s)
    letter_set = set()
    ans, i, j = 0, 0, 0
    while i<n and j < n:
        print(j)
        if s[j] not in letter_set:
            letter_set.add(s[j])
            j += 1
            ans =max(ans, j-i)
            print('not in letter_set is {}'.format(letter_set))
        else:
            print('i is {}, {} to be removed '.format(i, s[i]))
            print(' i is {} , remove {}'.format(i ,s[i]))
            letter_set.remove(s[i])
            print('in letter_set is {}'.format(letter_set))
            i+=1
    print(letter_set)
    return ans

# def l3(s):
    # if s is None and len(s) == 0:
        # return 0

    # cur = 0
    # res = 0
    # letter_last_pos = [-1 for i in range(256)]
    # i, j = 0, 0
    # while j < len(s):
        # # not exist
        # if letter_last_pos[ord(s[j])] == -1:
            # letter_last_pos[ord(s[j])] = j
            # print('{}    {}'.format(i, j))
            # cur = j - i + 1
            # j += 1
            # # print(letter_last_pos)
        # else:
            # # letter_last_pos[ord(s[i])] = -1
            # left  = letter_last_pos[ord(s[j])]
            # # print('exit pos is {}'.format(i))
            # cur = j - left + 1
            # letter_last_pos[ord(s[j])] = j
            # i = left + 1
            # j += 1
            # # print(letter_last_pos)
        # res = max(res, cur)
#     return res
if __name__ == "__main__":
    print('*'*80)
    sol = Solution()
    # res = sol.lengthOfLongestSubstring("abcabcbb")
    test_str = 'abcabcbb'
    res = sol.lengthOfLongestSubstring2("abcabcbb")
    print(res)
    # test_str = 'aab'
    # print(l3(test_str))
    # l = [1,2,3,4,5]
    # print(l[int('a')])
    # print(ord('a'))
    # l = [6,4,3,2,9]
    # s = set()
    # for i in range(5):
        # s.add(l[i])
    #     print(s)
