from linked_list.list_op import *
from copy import deepcopy


class Solution_0:
    successor = None

    def reverse_top_n(self, head, num):
        if num == 1:
            self.successor = head.next
            return head
        last = self.reverse_top_n(head.next, num - 1)
        head.next.next = head
        head.next = self.successor
        return last


class Solution_00:
    def reverse_top_n(self, head, count):
        if head is None:
            return None
        origin = head
        cur = head
        for i in range(count - 1):
            cur = cur.next

        cur_next = cur.next
        root = self.helper(head, count)
        origin.next = cur_next
        return root

    def helper(self, head, count):
        tmp = head
        i = 1
        while i < count and tmp is not None:
            tmp = tmp.next
            i += 1
        if tmp is None:
            return head

        if count == 1:
            return head

        # new_root不可以使用它来进行链表的操作, 目的就是返回节点，充当头指针
        new_root = self.helper(head.next, count - 1)

        # 操作比较花哨，只使用head完成下一个节点指向自身节点
        head.next.next = head
        head.next = None
        return new_root


if __name__ == '__main__':
    head = create_list([1, 2, 3, 4, 5, 6])
    # print_list(head)
    sol = Solution()
    head = sol.reverse_top_n(head, 3)
    print_list(head)
