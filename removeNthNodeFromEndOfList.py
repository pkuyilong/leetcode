# -*- coding: utf-8 -*-
# 2018-11-07 17:51 mayilong 

import os
import sys
import numpy as np

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if n == 0:
            return head
        dummy = ListNode(0)
        slow = dummy
        fast = dummy
        dummy.next = head
        for i in range(n+1):
            if fast is not None:
                fast = fast.next
            else:
                dummy.next = dummy.next.next
                return dummy.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next



if __name__ == "__main__":
    print('*'*80)
    pass
