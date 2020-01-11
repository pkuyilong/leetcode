# -*- coding: utf-8 -*-
# Copyright © 2018 mayilong <mayilong@mayilong.local>

"""

"""

def test():
    
    pass

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        fast = dummyNode
        slow = dummyNode
        for i in range(n+1):
            if fast:
                fast = fast.next
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummyNode.next



if __name__ == "__main__":
    print("*"*80)
    test()

    pass
