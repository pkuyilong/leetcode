# 264. 丑数 II
# https://leetcode-cn.com/problems/ugly-number-ii/

import sys


class Solution_0:
    """
    这种方法会work，但是会超时
    从当前值开始计算，如果它能被2整除，而且它的值为丑数，那么当前值也是丑数
    同理，除以三和五也一样
    """

    def nthUglyNumber(self, n: int) -> int:
        ugly_set = {1}
        count = 1

        if n == 1:
            return 1

        i = 2
        while i < sys.maxsize:
            if i % 2 == 0:
                if i // 2 in ugly_set:
                    ugly_set.add(i)
                    count += 1
                    if count == n:
                        return i
                    i += 1
                else:
                    i += 1
                    continue

            elif i % 3 == 0:
                if i // 3 in ugly_set:
                    ugly_set.add(i)
                    count += 1
                    if count == n:
                        return i
                    i += 1
                else:
                    i += 1
                    continue

            elif i % 5 == 0:
                if i // 5 in ugly_set:
                    ugly_set.add(i)
                    count += 1
                    if count == n:
                        return i
                    i += 1
                else:
                    i += 1
                    continue
            else:
                i += 1
        return -1


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        index2, index3, index5 = 1, 1, 1
        for i in range(2, n + 1):
            # 都是以之前的丑数为基准的
            dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)
            while dp[index2] * 2 <= dp[i]:
                index2 += 1
            while dp[index3] * 3 <= dp[i]:
                index3 += 1
            while dp[index5] * 5 <= dp[i]:
                index5 += 1
            print(dp)
            print(index2, index3, index5)
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    res = sol.nthUglyNumber(15)
    print(res)
