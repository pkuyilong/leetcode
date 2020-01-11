# 160. 相交链表
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/


"""
编写一个程序，找到两个单链表相交的起始节点。
"""


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        两个节点走完自己的链，然后接着走别人的链，一定会碰头的
        1. p1走自己的链， p2走自己的链
        2. 如果p1走完了，则去走p2的链，同理p2
        """
        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB
        flag1 = False
        flag2 = False
        while not (flag1 and flag2):
            while p1 and p2:
                if p1 == p2:
                    return p1
                p1 = p1.next
                p2 = p2.next
                if not flag1 and p1 is None:
                    p1 = headB
                    flag1 = True
                if not flag2 and p2 is None:
                    p2 = headA
                    flag2 = True
        return None
