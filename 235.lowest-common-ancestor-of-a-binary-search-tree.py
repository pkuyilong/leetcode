# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/

"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    两个节点p q的公共祖先N, 有两种情况
        1. p在公共祖先N的左子树中 and q在公共祖先N右子树中
        2.q在公共祖先N的左子树中 and p在公共祖先N右子树中
    因为题目限定了是二叉搜索树
        1. 左子树的节点的值都小于其父节点的值
        2. 柚子树的节点的值都大于其父节点的值
    """
    def lowestCommonAncestor(self, root, p, q):
        if p is root or q is root:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if self.inTree(root.left, p) and self.inTree(root.right, q):
            return root
        if self.inTree(root.left, q) and self.inTree(root.right, p):
            return root
        return None

    def inTree(self, root, node):
        if root is None:
            return False

        if root is node:
            return True

        if node.val < root.val:
            return self.inTree(root.left, node)
        else:
            return self.inTree(root.right, node)
