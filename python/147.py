# 147. 对链表进行插入排序
# https://leetcode-cn.com/problems/insertion-sort-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        cur = head
        while cur:
            if cur.next:
                if cur.val < cur.next.val:
                    cur = cur.next
                else:
                    # 此时cur.val >= cur.next.val, cur需要移动到下一个节点，才是要交换的节点
                    cur = cur.next
                    self.change_order(head, cur)
            # 如果cur为最后一个元素，那么终止循环
            else:
                break
        return head

    def change_order(self, root, end):
        """
        从链表头部开始遍历，如果node的值小于end的值，交换位置, node移动到下一个元素，
        直到node == end，完成排序
        :param root: 链表头节点
        :param end: 要交换的节点
        :return:
        """
        p = root
        while p != end:
            if p.val > end.val:
                p.val, end.val = end.val, p.val
            p = p.next
        # self.p(root)

    # def p(self, root):
    #     cur = root
    #     while cur:
    #         print(cur.val)
    #         cur = cur.next
    #     print("#" * 50)


if __name__ == '__main__':
    root = ListNode(5)
    root.next = ListNode(7)
    root.next.next = ListNode(8)
    root.next.next.next = ListNode(6)
    root.next.next.next.next = ListNode(2)
    root.next.next.next.next.next = ListNode(1)
    sol = Solution()
    sol.insertionSortList(root)
    cur = root
    while cur:
        print(cur.val)
        cur = cur.next
