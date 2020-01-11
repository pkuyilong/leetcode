class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(nums):
    head = None
    if head is None:
        head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        tmp_node = ListNode(nums[i])
        cur.next = tmp_node
        cur = tmp_node
    return head


def print_list(head):
    print("Print Start")
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
    print("Print Done")
