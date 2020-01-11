# -*- coding: utf-8 -*-
# 2018-11-22 15:31 mayilong 

import os
import sys
import numpy as np


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(root):
    if root is None or root.next is None:
        return root
    p = root
    q = root.next
    root.next = None
    tmp = q
    while q:
        tmp = q.next
        q.next = p
        p = q
        q = tmp
    return p




if __name__ == "__main__":
    root=ListNode(0)
    # node1= ListNode(1)
    # root.next = node1
    r = reverseList(root)
    while r:
        print(r.val)
        r = r.next
    print('*'*80)
    pass
