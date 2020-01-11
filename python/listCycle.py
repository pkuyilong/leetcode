# -*- coding: utf-8 -*-
# 2018-11-07 17:30 mayilong 

import os
import sys
import numpy as np


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head
        # forget fast is not None
        # while fast is not None and fast.next is not None:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True




if __name__ == "__main__":
    print('*'*80)
    pass
