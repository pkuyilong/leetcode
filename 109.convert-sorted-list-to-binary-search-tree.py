# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    先找到链表的中点，然后将数据划分成左半边和右半边
    """

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        dummy_node = TreeNode(-1)
        dummy_node.next = head
        # prev是最中间节点的前一个，目的就是为了拆分链表
        prev = dummy_node
        fast = prev.next
        slow = prev.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next
        # 注意将数组打断
        prev.next = None

        # 构建当前根结点并递归构建左右子树节点
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
