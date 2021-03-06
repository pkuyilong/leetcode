# 98. 验证二叉搜索树
# https://leetcode-cn.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
    中序遍历是左子树 根节点 右子树
"""


class Solution:
    prev = None

    def isValidBST(self, root):
        if root is None:
            return True
        left = self.isValidBST(root.left)
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        right = self.isValidBST(root.right)
        return left and right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nums = list()
        self.helper(root, nums)
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return False
        return True

    def helper(self, root, nums):
        if root is None:
            return
        self.helper(root.left, nums)
        nums.append(root.val)
        self.helper(root.right, nums)
