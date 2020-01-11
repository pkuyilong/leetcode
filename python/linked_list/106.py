# 206. 反转链表
# https://leetcode-cn.com/problems/reverse-linked-list/

"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""

class Solution:
    def __init__(self):
        self.root = None

    def reverseList(self, head):
        if head is None:
            return head
        self.reverse_helper(head)
        return self.root

    def reverse_helper(self, head):
        """
        新的理解，对于递归函数仿佛就是一个分段函数，每一个返回的函数从这里开始执行
        第1段：self.reverse_helper(head.next) 之前的
        第2段：self.reverse_helper(head.next) 之后的
        """
        # 这个地方只会被执行一次， 使用self.root记录下最终的头结点
        if head.next is None:
            self.root = head
            return head

        node = self.reverse_helper(head.next)

        node.next = head
        head.next = None
        return head
