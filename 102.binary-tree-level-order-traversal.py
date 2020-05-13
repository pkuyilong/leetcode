# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return list()
        ans = list()
        node_list = list()
        node_list.append(root)
        while len(node_list) > 0:
            prev_len = len(node_list)
            tmp_ans = list()
            for i in range(prev_len):
                tmp_node = node_list.pop(0)
                tmp_ans.append(tmp_node.val)
                if tmp_node.left is not None:
                    node_list.append(tmp_node.left)
                if tmp_node.right is not None:
                    node_list.append(tmp_node.right)

            ans.append(tmp_ans)
        return ans