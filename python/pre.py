# -*- coding: utf-8 -*-
# 2018-11-07 10:10 mayilong 

import os
import sys
import numpy as np

def pre(root):
    l = []
    s = []
    if root is none:
        return l
    s.append(root)
    while len(s):
        tmp = s.pop()
        l.append(tmp.val)
        if tmp.right:
            s.append(tmp.right)
        if tmp.left:
            s.append(tmp.left)




if __name__ == "__main__":
    
    print('*'*80)
    pass
