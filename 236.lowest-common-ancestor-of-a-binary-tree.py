# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 终止条件 如果当前节点是None 或者等于p 或者q，那么返回
        if root is None or p == root.val or q == root.val:
            return root

        # 先在某一个分支上找到其中的一个节点
        left_side = self.lowestCommonAncestor(root.left, p, q)
        right_side = self.lowestCommonAncestor(root.right, p, q)
        # 如果某一个节点下左子树和右子树分别找到了p和q，那么当前节点就是最近的公共祖先
        if left_side and right_side:
            return root
        # 返回的节点要么是None 要么是p或者q节点
        return left_side if right_side is None else right_side


class BST:
    def __init__(self, nums):
        super(BST, self).__init__()
        self.root = self.construct(nums, 0, len(nums) - 1)

    def construct(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.construct(nums, left, mid - 1)
        root.right = self.construct(nums, mid + 1, right)
        return root

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.val)
        self.inOrder(root.right)


if __name__ == '__main__':
    nums = [3, 9, 10, 2, 5, 4, 8]
    bst = BST(nums)
    # print("####" * 20)
    # bst.inOrder(bst.root)

    sol = Solution()
    node = sol.lowestCommonAncestor(bst.root, 8, 4)
    print(node.val)

