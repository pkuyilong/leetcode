# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    二叉搜索树的中序遍历是递增的

    """

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.helper(nums, 0, len(nums) - 1)
        return root

    def helper(self, nums, left, right):
        if left > right:
            return
        # 选取中间节点作为根结点，那么他的左子树节点可以递归的调用左边的数字，右边同理
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root
