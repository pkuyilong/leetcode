# -*- coding: utf-8 -*-
# 2018-11-15 11:34 mayilong 

import os
import sys
import numpy as np

def remove(s):
    if s is None or len(s) == 0:
        return s
    l = []
    idx = 0
    while idx < len(s) and s[idx] == " ":
        idx += 1
    while idx < len(s):
        if s[idx] != ' ':
            l.append(s[idx])
            idx += 1
        elif idx > 0 and s[idx-1] != ' ' and s[idx] == ' ':
            l.append(s[idx])
            idx += 1
        else:
            idx += 1
            continue

    j = len(l)-1
    while j > 0 and l[j] == " " :
        l.pop()
        j -= 1
    return "".join(l)


if __name__ == "__main__":
    s = '  somone unser    the tree  '
    print(remove(s))
    print('*'*80)
    pass
