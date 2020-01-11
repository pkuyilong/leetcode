# -*- coding: utf-8 -*-
# 2018-11-14 23:08 mayilong 

import os
import sys
import numpy as np
def string_to_interge(s):
    if s is None:
        return 0
    if len(s) is 0:
        return 0
    ng = 1
    if s[0] == '-':
        ng = -1
    else:
        ng = 1
    l = s.split('.')
    num = 0
    num1 = 0.0
    if len(l) == 1:
        assert len(l) == 1
        print(l[0])
        for i in range(len(l[0])):
            num = num*10 + int(l[0][i])

    if len(l) == 2:
        for i in range(len(l[0])):
            num = num*10 + int(l[0][i])
        for i in range(len(l[1])-1,0, -1):
            num1 = num1 * 0.1 + int(l[1][i])
        print(num1)
    return (num + num1)*ng


if __name__ == "__main__":
    print('*'*80)
    print(string_to_interge('120.334'))
    # s = set()
    # for item in nums:
        # if item not in s:
            # s.add(item)
        # els4:
    #         print(item)
    pass
