
# https://leetcode-cn.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        node_list = list()
        self.inOrder(root, node_list)
        root = self.build(node_list)
        return root

    def inOrder(self, root, node_list):
        if root is None:
            return
        self.inOrder(root.left, node_list)
        node_list.append(root.val)
        self.inOrder(root.right, node_list)

    def build(self, node_list):
        l, r = 0, len(node_list) - 1
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(node_list[mid])
        root.left = self.build(node_list[:mid])
        root.right = self.build(node_list[mid + 1:])
        return root