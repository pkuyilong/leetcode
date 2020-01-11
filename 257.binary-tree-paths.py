# 257. 二叉树的所有路径
# https://leetcode-cn.com/problems/binary-tree-paths/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = list()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.dfs(root, [])
        return self.res

    def dfs(self, root, tmp_list):
        if root:
            tmp_list.append(str(root.val))

            if root.left is None and root.right is None:
                self.res.append("->".join(tmp_list))

            self.dfs(root.left, tmp_list)
            self.dfs(root.right, tmp_list)
            tmp_list.pop()
