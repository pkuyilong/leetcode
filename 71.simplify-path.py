# 71. 简化路径
# https://leetcode-cn.com/problems/simplify-path

from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        """思路
            1. 对字符串按照 '/'进行分割，获取到每个元素，过滤掉空的元素，剩下的元素会构成字符串
            2. 使用双向队列，按照各种符号进行操作(主要是 '.' 和 '..')，
                2.1 如果是字符串，那么直接追加到队列尾部
                2.2 如果是'.', 那么什么也不做，相当于停留在当前的路径上
                2.3 如果是'..', 把上一级的元素从队列尾部弹出， 相当于跳到上一级目录
            3. 合并路径

        """
        if path is None or len(path) == 0:
            return ""
        path_content = path.split('/')
        print(path_content)
        path_content = list(filter(lambda x: x != '', path_content))
        print(path_content)
        stk = deque()
        for item in path_content:
            if str.isalpha(item):
                stk.append(item)
            elif item == '.':
                continue
            elif item == '..':
                if len(stk):
                    stk.pop()
            else:
                stk.append(item)
        ret_path = '/'
        print(stk)
        while len(stk):
            ret_path += stk.popleft() + '/'
        ret_path = ret_path[:len(ret_path)-1] if len(ret_path) != 1 else ret_path
        return ret_path


if __name__ == '__main__':
    # path = "/a//b////c/d//././/.."
    path = '/...'
    sol = Solution()
    res = sol.simplifyPath(path)
    print(res)
