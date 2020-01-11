# -*- coding: utf-8 -*-
# 2018-11-22 20:32 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from collections import defaultdict


def test(s):
    if s is None or len(s) == 0:
        return 0
    i, j = 0,0
    d = defaultdict(int)
    ch_set = set()
    len_max = 0
    cur = 0
    while j < len(s):
        if s[j] not in ch_set:
            ch_set.add(s[j])
            cur = j - i + 1
            len_max = max(cur, len_max)
            j += 1
        else:
            ch_set.remove(s[i])
            i += 1
    return len_max

def test2(s):
    if s is None and len(s) == 0:
        return 0
    i, j = 0, 0
    d = defaultdict(int)
    ch_set = set()
    cur = 0
    len_max = 0
    while j < len(s):
        if s[j] not in ch_set:
            d[s[j]] = j
            ch_set.add(s[j])
            cur = j - i + 1
            len_max = max(len_max, cur)
            j += 1
        else:
            tmp = d[s[j]]
            while i <= tmp:
                ch_set.remove(s[i])
                i += 1
    return len_max



if __name__ == "__main__":
    print('*'*80)
    print(test2('abcabcbb'))
    pass
