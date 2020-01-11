# -*- coding: utf-8 -*-
# Copyright © 2018 mayilong <mayilong@bogon>

"""

"""
import pdb
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
p   n1  n2  n
"""

class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return head
        dummyNode = ListNode(-1)
        dummyNode.next = head
        p = dummyNode
        while p and p.next and p.next.next:
            # pdb.set_trace()
            n1 = p.next
            n2 = n1.next
            n = n2.next

            n2.next = n1
            n1.next = n
            p.next = n2
            p = n1
        return dummyNode.next
     

if __name__ == "__main__":
    print("*"*80)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next  = ListNode(3)
    head.next.next.next  = ListNode(4)

    it = head
    while it:
        print(it.val)
        it = it.next

    sol = Solution()
    head = sol.swapPairs(head)
    it = head
    print("*****")
    while it:
        print(it.val)
        it = it.next
    
