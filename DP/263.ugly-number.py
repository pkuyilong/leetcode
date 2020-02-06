# 263. 丑数
# https://leetcode-cn.com/problems/ugly-number/


"""思路
    1. 如果是丑数，那么肯定是2、3、5的乘积
    2. 当num能被2、 3、 5任意一个数子整除，那么num = num // (2 or 3 or 5)
    3. 重复2步骤，直到num == 1 或者 num不能被（2、3、5)任意一个整除

"""


class Solution:
    def isUgly(self, num):
        if num < 1:
            return False
        while num != 1:
            if num % 5 == 0:
                num = num // 5
            elif num % 3 == 0:
                num = num // 3
            elif num % 2 == 0:
                num = num // 2
            else:
                return False
        return True


"""
这个版本类似于换零钱的解法
# 322. 零钱兑换
# https://leetcode-cn.com/problems/coin-change/

但会超时

大的问题依赖于子问题
dp[i] = (dp[i//3], dp[i//5], dp[i//2])  if i 能被2或3或5整除
"""


class Solution_0:
    def isUgly(self, num):
        if num < 1:
            return False
        dp = [False for i in range(num + 1)]
        dp[1] = True
        for i in range(num + 1):
            for factor in [2, 3, 5]:
                if i >= factor:
                    if i % factor == 0:
                        if dp[i // factor] is True:
                            dp[i] = True
        # print(dp)
        return dp[num]


if __name__ == '__main__':
    res = Solution_0().isUgly(6)
    print(res)
