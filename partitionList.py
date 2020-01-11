# -*- coding: utf-8 -*-
# Copyright © 2018 mayilong <mayilong@bogon>

"""

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        arr1 = []
        arr2 = []
        p = head
        while p:
            if p.val < x:
                arr1.append(p.val)
            else:
                arr2.append(p.val)
            p = p.next
        dummyNode = ListNode(0)
        p = dummyNode
        arr = arr1 + arr2
        print(arr)
        for i in range(len(arr)):
            tmp = ListNode(arr[i])
            p.next = tmp
            p = p.next
        return dummyNode.next

if __name__ == "__main__":
    print("*"*80)
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next  = ListNode(3)
    head.next.next.next  = ListNode(2)
    sol = Solution()
    head = sol.partition(head, 3)
    it = head 
    while it:
        print(it.val)
        it = it.next

    pass
