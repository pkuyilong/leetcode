# 199. 二叉树的右视图
# https://leetcode-cn.com/problems/binary-tree-right-side-view/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from copy import deepcopy
# 层次遍历
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res_list = []
        cur_list = []
        next_list = []
        cur_list.append(root)
        res_list.append(cur_list[-1].val)
        while cur_list:
            while cur_list:
                tmp = cur_list.pop(0)
                if tmp.left:
                    next_list.append(tmp.left)
                if tmp.right:
                    next_list.append(tmp.right)
            if len(next_list) != 0:
                res_list.append(next_list[-1].val)
            cur_list = deepcopy(next_list)
            next_list.clear()
        return res_list



# 深度优先搜索
class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res_list = []
        self.dfs(root, res_list, 0)
        return res_list


    def dfs(self, root, res_list, depth):
        if root:
            if depth == len(res_list):
                res_list.append(root.val)
            else:
                res_list[depth] = root.val

            self.dfs(root.left, res_list, depth + 1)
            self.dfs(root.right, res_list, depth + 1)
