#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 alex <alex@localhost>
#
# Distributed under terms of the MIT license.

"""

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
    def getIntersectionNode(self, headA, headB):
        # 两个指针同时前进, 如果其中一个到了结尾，就跑到另一个链表头上去，继续进行
        # 如果存在交叉点，那么两者一定会相遇。如果不存在交叉点，两者应该同时为None，
        # 此时退出循环。
        # 有一种特殊情况，就是两条链表没有交点，但是其长度一样，这种情况不处理会陷入死循环。
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        tmpA = headA
        tmpB = headB

        while tmpA and tmpB:
            if tmpA == tmpB:
                return tmpA

            tmpA = tmpA.next
            tmpB = tmpB.next

            if tmpA is None and tmpB is None :
                return None

            if tmpA is None:
                tmpA = headB

            if tmpB is None:
                tmpB = headA

        return None

def build_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in range(1, len(nums)):
        tmpNode = ListNode(num)
        cur.next = tmpNode
        cur = cur.next
    return head

if __name__ == '__main__':
    sol = Solution()
    headA = build_list([4,1,8,4,5])
    headB = build_list([5,0,1,8,4,5])

    result = sol.getIntersectionNode(headA, headB)
    print(result.val)
