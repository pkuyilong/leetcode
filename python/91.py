# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/


class Solution:
    """ Time excess limit
    这里进行了不断的递归，分解子问题

    """
    def __init__(self):
        self.count = 0
        self.s = set()
        self.d = dict()

    def numDecodings(self, s):
        self.helper(s)
        return self.count

    def helper(self, s):
        if s in self.d.keys():
            return self.d[s]

        if s == "":
            self.count += 1
            return

        if len(s) == 1:
            if self.is_valid(s):
                self.count += 1
                return
        else:
            for i in range(1, 3):
                cur = s[:i]
                if self.is_valid(cur):
                    self.helper(s[i:])


    def is_valid(self, s):
        if s is None or s == "":
            return False
        if s.startswith('0'):
            return False
        if int(s) > 26:
            return False
        return True


if __name__ == '__main__':
    import time

    s = "123678999999"*4
    sol = Solution()
    start = time.time()
    count = sol.numDecodings(s)
    print(time.time() - start)
    print("res is :", count)
