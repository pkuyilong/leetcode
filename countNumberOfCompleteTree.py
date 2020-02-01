class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1

    def getLeaveNodes(self, root, count):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            count += 1
            return count
        left_count = self.getLeaveNodes(root.left, count)
        right_count = self.getLeaveNodes(root.right, count)
        return left_count + right_count

    def numOfKLayer(self, root, k):
        if root is None or k < 1:
            return 0
        left = self.numOfKLayer(root.left, k - 1)
        right = self.numOfKLayer(root.right, k - 1)
        if k == 1:
            return 1
        return left + right


if __name__ == "__main__":
    print('*' * 80)
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(7)

    sol = Solution()
    count = 0
    # res = sol.countNodes(root)
    # num = sol.getLeaveNodes(root, count)
    print(sol.numOfKLayer(root, 4))
    pass
