# -*- coding: utf-8 -*-
# 2018-12-25 11:44 mayilong 

import os
import sys
import numpy as np
import torch
import torch.nn as nn
from torchvision import models
import torch.nn.functional as F

class SingleRNN(nn.Module):
    def __init__(self, n_inputs, n_neurons):
        super().__init__()

        self.Wx = torch.randn(n_inputs, n_neurons)
        self.Wy = torch.randn(n_neurons, n_neurons)

        self.b = torch.zeros(1, n_neurons)

    def forward(self, X0, X1):
        self.Y0 = torch.tanh(torch.mm(X0, self.Wx) + self.b)
        print("X0 size : {}, Wx size is {},  Y0 size : {}"
                .format(X0.size(), self.Wx.size(), self.Y0.size()))

        self.Y1 = torch.tanh(torch.mm(self.Y0, self.Wy) + torch.mm(X1, self.Wx) + self.b)
        print("X1 size : {}, Wy size is {},  Y1 size : {}"
                .format(X1.size(), self.Wx.size(), self.Y1.size()))

        return self.Y0, self.Y1


if __name__ == "__main__":
    print('*'*80)

    N_INPUT = 4
    N_NEURONS = 1

    X0_batch = torch.tensor([[0,1,2,0],
                             [3,4,5,0],
                             [6,7,8,0],
                             [9,0,1,0]],
                             dtype = torch.float)      ## 4*4

    X1_batch = torch.tensor([[9,8,7,0],
                             [0,0,0,0],
                             [6,5,4,0],
                             [3,2,1,0]],
                             dtype = torch.float)

    model = SingleRNN(N_INPUT, N_NEURONS)

    Y0_val , Y1_val = model(X0_batch, X1_batch)
    print(Y0_val)
    print(Y1_val)

