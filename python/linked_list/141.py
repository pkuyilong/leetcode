# 141. 环形链表
# https://leetcode-cn.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        if head is not None and head.next is None:
            return False
        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False