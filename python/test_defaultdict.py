# -*- coding: utf-8 -*-
# 2018-11-22 16:03 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from collections import defaultdict


def test():
    d = defaultdict()
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(sorted(d.items()))
    pass

if __name__ == "__main__":
    print('*'*80)
    test()
    pass
