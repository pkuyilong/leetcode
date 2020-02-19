# 206. 反转链表
# https://leetcode-cn.com/problems/reverse-linked-list/

"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
from linked_list.list_op import *


class Solution_1:
    root = None

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


class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        root = self.helper(head)
        return root

    def helper(self, head):
        if head.next is None:
            return head
        # 这个node一旦返回，不可以使用它来进行链表的操作
        # 它的意义目的就是返回最后一个链表节点， 充当头指针
        node = self.helper(head.next)

        # 因此这里的操作就比较花哨， 只能使用head也就是当前指针来操作指针，
        # 使其下一个节点的next节点指向自己
        head.next.next = head
        head.next = None
        return node

    # test
    def last_node(self, head):
        if head.next is None:
            return head
        node = self.last_node(head.next)
        return node


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = create_list(nums)
    print_list(head)
    sol = Solution_1()
    new_head = sol.reverseList(head)
    print_list(new_head)
