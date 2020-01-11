class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates2(self, head):
        res = list()
        if head is None:
            return res
        if head.next:
            p = head
            q = head.next
        while q:
            if p.val == q.val:
                while q and  p.val == q.val:
                    q = q.next
                if q is None:
                    p.next = q
                    break
                p.next = q
                p = q
                q = q.next
            else:
                p.next = q
                p = q
                q = q.next

        p1 = head
        while p1:
            res.append(p1.val)
            p1 = p1.next
        print(res) 
        return res


    def deleteDuplicates3(self, head):
        if head is None:
            return
        if head.next:
            p = head
            q = head.next
        while q:
            if p.val == q.val:
                while q and p.val == q.val:
                    q = q.next
                if not q:
                    p.next = q
                    break
            p.next = q
            p = q
            q = q.next
        p1 = head
        res = list()
        while p1:
            res.append(p1.val)
            p1 = p1.next
        print(res)

    def deleteDuplicates(self, head):
        if not head:
            return head
        cur =head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        p1 = head
        while p1:
            print(p1.val)
            p1 = p1.next



if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 3, 4, 4, 5]
    head = ListNode(1)
    ph = head
    for item in nums:
        ph.next = ListNode(item)
        ph = ph.next
    p = head
    while p:
        print(p.val)
        p = p.next
    print('*'*80)
    sol = Solution()
    sol.deleteDuplicates(head)
    # while head:
    #     print(head.val)
    #     head = head.next


