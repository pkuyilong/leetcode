# 206. 反转链表
# https://leetcode-cn.com/problems/reverse-linked-list/

"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
import sys

sys.path.append("../..")
from linked_list.list_op import *


class Solution:
    def reverseList(self, head, count):
        if head is None:
            return None
        origin = head
        cur = head
        for i in range(count - 1):
            cur = cur.next

        cur_next = cur.next
        root = self.helper(head, 0, count)
        origin.next = cur_next
        return root

    def helper(self, head, cur_count, count):
        if cur_count + 1 == count:
            return head

        # 这个node一旦返回，不可以使用它来进行链表的操作
        # 它的意义目的就是返回最后一个链表节点， 充当头指针
        node = self.helper(head.next, cur_count + 1, count)

        # 因此这里的操作就比较花哨， 只能使用head也就是当前指针来操作指针，
        # 使其下一个节点的next节点指向自己
        head.next.next = head
        head.next = None
        return node


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head = create_list(nums)
    sol = Solution()
    new_head = sol.reverseList(head, 5)
    print_list(new_head)
