
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p == root or q == root:
            return root

        # 先在某一个分支上找到其中的一个节点
        left_side = self.lowestCommonAncestor(root.left, p, q)
        right_side = self.lowestCommonAncestor(root.right, p, q)
        # 两个节点路径上最低的点都找到了
        if left_side and right_side:
            return root
        # 如果只找到一个节点的路径山最低的点， 则返回
        return left_side if right_side is None else right_side