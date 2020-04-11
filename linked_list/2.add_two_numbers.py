# 2. 两数相加
# https://leetcode-cn.com/problems/add-two-numbers/


from linked_list.list_op import *


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return l1 if l2 is None else l2
        res = ListNode(-1)
        cur = res
        carry = 0

        while l1 and l2:
            tmp = l1.val + l2.val + carry
            if tmp > 9:
                tmp = tmp - 10
                carry = 1
            else:
                carry = 0

            cur.next = ListNode(tmp)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        if l2 is None:
            while l1:
                tmp = l1.val + carry
                if tmp > 9:
                    tmp = tmp - 10
                    carry = 1
                else:
                    carry = 0
                cur.next = ListNode(tmp)
                cur = cur.next

                l1 = l1.next

        if l1 is None:
            while l2:
                tmp = l2.val + carry
                if tmp > 9:
                    tmp = tmp - 10
                    carry = 1
                else:
                    carry = 0
                cur.next = ListNode(tmp)
                cur = cur.next

                l2 = l2.next
        if carry == 1:
            cur.next = ListNode(1)
        return res.next


if __name__ == '__main__':
    l1 = create_list([1, 8])
    l2 = create_list([0])
    sol = Solution()
    new_l = sol.addTwoNumbers(l1, l2)
    print_list(new_l)
