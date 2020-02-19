from linked_list.list_op import create_list, print_list


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


class Solution:
    successor = None

    def reverse_top_n(self, head, num):
        if num == 1:
            self.successor = head.next
            return head
        last = self.reverse_top_n(head.next, num - 1)
        head.next.next = head
        head.next = self.successor
        return last

if __name__ == '__main__':
    head = create_list([1, 2, 3, 4, 5, 6])
    # print_list(head)
    sol = Solution()
    head = sol.reverse_top_n(head, 1)
    print_list(head)
    print(sol.successor.val)
