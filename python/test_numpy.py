# -*- coding: utf-8 -*-
# 2018-11-17 12:32 mayilong 

import os
import sys
import numpy as np
import torch


def test():
    x = np.tile([0,1], (3, 5))
    print(x)
    y = np.random.randn(64,3,7,7)
    print(y.shape)
    z = y[:,:,:,:, np.newaxis]
    print(z.shape)
    q = np.tile(z, (1, 1, 1, 1, 7))
    print(q.shape)
    print(q[:, :, :, :, 1] == q[:, :, :, :, 5])

def test2():
    x = torch.randn(64, 3, 7, 7)
    x = x.unsqueeze(4)
    print(x.size())
    y = x.repeat([1,1,1,1,7])
    print(y.size())
    print(y[:, :, :, :, 1] == y[:, :, :, :, 5])



if __name__ == "__main__":
    print('*'*80)
    test2()
    pass
