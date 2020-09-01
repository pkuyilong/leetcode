
"""
我小看了这道题目
判断是不是子树问题和判断是不是同一颗树的问题, 本质上是一样的

一个是判断节点的值相不相同
另一个就是判断树相不相同
"""



class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # 这是递归结束条件, 而不是开始的判断条件
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False

        if self.isSame(s, t):  ### 1
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t):
        # 这是递归结束条件,不是开始判断条件
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False

        if s.val != t.val: #### 2
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
