# 117. 填充每个节点的下一个右侧节点指针 II
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
from copy import copy


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        nxt = []
        cur = [root]
        root.next = None

        while cur:
            while cur:
                tmp = cur.pop(0)
                if tmp.left:
                    nxt.append(tmp.left)
                if tmp.right:
                    nxt.append(tmp.right)
            if len(nxt) != 0:
                for i in range(len(nxt) - 1):
                    nxt[i].next = nxt[i + 1]
                nxt[len(nxt) - 1].next = None
            # 这里如果用deepcopy的话，你会爽歪歪！！！ 你要用原来的树节点，而不是deepcopy创建的新节点
            cur = copy(nxt)
            nxt.clear()
        return root
