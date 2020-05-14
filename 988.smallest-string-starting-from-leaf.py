# 988. 从叶结点开始的最小字符串
# https://leetcode-cn.com/problems/smallest-string-starting-from-leaf/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def __init__(self):
        self.ans = "~"

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, A):
        if root:
            A.append(chr(root.val + ord('a')))
            if root.left is None and root.right is None:
                self.ans = min(self.ans, "".join(reversed(A)))

            self.dfs(root.left, A)
            self.dfs(root.right, A)
            A.pop()



if __name__ == '__main__':
    nums = [25, 1, 3, 1, 3, 0, 2]
    alphas = [chr(num + ord('a')) for num in nums]
    print(alphas)
