# 116. 填充每个节点的下一个右侧节点指针
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            if root.left is None and root.right is None:
                return root
            if root.left:
                root.left.next = root.right
            if root.right:
                if root.next:
                    root.right.next = root.next.left
                else:
                    root.right.next = None

            root.left = self.connect(root.left)
            root.right = self.connect(root.right)
        return root
