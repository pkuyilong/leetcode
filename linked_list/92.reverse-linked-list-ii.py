# 92. 反转链表 II
# https://leetcode-cn.com/classic/problems/reverse-linked-list-ii/


"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""

from linked_list.list_op import create_list, print_list


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_0(object):
    """ 思路
        1. 截取出需要翻转的部分
            1.1 记录下需要翻转的节点m，以及m的前一个节点
            1.2 需要翻转的链表尾部节点n以及n的下一个节点
        2. 翻转后接入到来的链表中
    """

    def reverseBetween(self, head, m, n):
        if head is None:
            return head

        pre = None
        cur = head
        i = 0
        while i < m - 1:
            pre = cur
            cur = cur.next
            i += 1
        last_node = cur

        tmp = cur
        while i < n - 1:
            cur = cur.next
            i += 1
        post_node = cur.next

        new_root = self.reverse_helper(tmp, 0, n - m + 1)
        # 需要判断pre是不是为None， 也就是判断是不是从链表的第一个节点就开始翻转了
        if pre is not None:
            pre.next = new_root
        else:
            head = new_root
        last_node.next = post_node
        return head

    def reverse_helper(self, root, cur_count, total):
        if cur_count + 1 == total:
            return root
        node = self.reverse_helper(root.next, cur_count + 1, total)
        root.next.next = root
        root.next = None
        return node


class Solution(object):
    """ 思路
        1. 如果m==1，那么这个题目就是翻转一个链表的前n个节点
        2. 如果m!=1, 假设原始链表的头结点是C，首先找到第m-1个节点（假设为A)保存下来，
        然后翻转以第m个节点为链表头的链表（返回新的头节点，假设为B)
        之后A.next = B就完成了，注意要返回原来的头结点
    """
    succesor = None

    def reverseBetween(self, head, m, n):
        if head is None:
            return head
        if m == 1:
            new_root = self.reverse_top_n(head, n)
            return new_root
        else:
            cur = head
            i = 2
            while i < m:
                cur = cur.next
                i += 1
            tmp_root = self.reverse_top_n(cur.next, n - m + 1)
            cur.next = tmp_root
            return head

    # 辅助函数，翻转一个链表的前n个节点
    def reverse_top_n(self, head, num):
        assert num >= 0, "Value error"
        if num == 1:
            self.succesor = head.next
            return head

        node = self.reverse_top_n(head.next, num - 1)
        head.next.next = head
        head.next = self.succesor
        return node


class Solution(object):
    """ 思路
        1. 如果m==1，那么这个题目就是翻转一个链表的前n个节点
        2. 如果m!=1, 假设原始链表的头结点是C，首先找到第m-1个节点（假设为A)保存下来，
        然后翻转以第m个节点为链表头的链表（返回新的头节点，假设为B)
        之后A.next = B就完成了，注意要返回原来的头结点C
    """
    succesor = None

    def reverseBetween(self, head, m, n):
        if head is None:
            return head
        if m == 1:
            new_root = self.reverse_top_n(head, n)
            return new_root
        else:
            head.next = self.reverseBetween(head.next, m - 1, n - 1)
            return head

        # 辅助函数，翻转一个链表的前n个节点

    def reverse_top_n(self, head, num):
        assert num >= 0, "Value error"
        if num == 1:
            self.succesor = head.next
            return head

        node = self.reverse_top_n(head.next, num - 1)
        head.next.next = head
        head.next = self.succesor
        return node


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    head = create_list(nums)
    print_list(head)
    sol = Solution()
    new_head = sol.reverseBetween(head, 1, 4)
    print_list(new_head)
