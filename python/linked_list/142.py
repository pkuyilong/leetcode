
# 142. 环形链表 II
# https://leetcode-cn.com/problems/linked-list-cycle-ii/

"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """" 问题分解
    1. 快慢指针第一次相遇，快指针比慢指针多走一个环的长度
    2. 利用两个指针找到环的入口点
        2.1 指针1还原到链表的头结点，指针2就是第一步中的慢指针
        2.2 指针1和指针2同步移动，每次移动一个位置，直到相遇

    """
    def detectCycle(self, head):
        if head is None:
            return None
        node = self.find_first_intersection(head)
        if node is None:
            return None
        p1 = head
        p2 = node
        while p1:
            # 这里的判断顺序也很重要
            if p1 == p2:
                break
            p1 = p1.next
            p2 = p2.next
        return p1

    def find_first_intersection(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 这种判断得先后顺序很重要, 如果放在while下边的第一行，
            # 那么直接就返回了，因为slow 和 fast 的初始值是一样的
            if fast == slow:
                return fast
        return None

