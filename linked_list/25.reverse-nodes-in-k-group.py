# 25. K 个一组翻转链表
# https://leetcode-cn.com/classic/problems/reverse-nodes-in-k-group/


"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        end = dummy.next
        start = dummy
        cur = head
        stack = deque()
        i = 0
        while cur is not None:
            while cur is not None and i < k:
                stack.append(cur)
                cur = cur.next
                i += 1

            if len(stack) != k:
                return dummy.next
            end = cur
            while len(stack) > 0:
                node = stack.pop()
                start.next = node
                start = start.next
            start.next = end
            i = 0
        return dummy.next
