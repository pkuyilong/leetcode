# 264. 丑数 II
# https://leetcode-cn.com/problems/ugly-number-ii/


"""
如果一个数是丑数，那么它的2倍、3倍、5倍都是丑数
反过来说，如果当前数字除以2 或者 除以5 或者 除以 3 为丑数，
那么这个数字就是丑数,
使用一个set保持前n-1个丑数，依次遍历即可
算法超时
"""

from queue import PriorityQueue


class Solution(object):
    def nthUglyNumber(self, n):
        q = PriorityQueue()
        answer = 1
        count = 1
        while count < n:
            q.put(answer * 2)
            q.put(answer * 3)
            q.put(answer * 5)

            answer = q.get()
            print(q)
            print(answer)
            count += 1
            while not q.empty():
                q.get()
            if count == n:
                return count


class Solution_3(object):
    def nthUglyNumber(self, n):
        s = set()
        count = 5
        if n <= 5:
            return n
        for i in range(1, 6):
            s.add(i)
        count = 5
        i = 6
        while count < n:
            if i % 5 == 0 and i // 5 in s:
                s.add(i)
                count += 1
            elif i % 3 == 0 and i // 3 in s:
                s.add(i)
                count += 1
            elif i % 2 == 0 and i // 2 in s:
                s.add(i)
                count += 1
            if count == n:
                return i
            i += 1


class Solution_1:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        index2, index3, index5 = 1, 1, 1
        for i in range(2, n + 1):
            # 都是以之前的丑数为基准的
            dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)
            if dp[index2] * 2 == dp[i]:
                index2 += 1
            if dp[index3] * 3 == dp[i]:
                index3 += 1
            if dp[index5] * 5 == dp[i]:
                index5 += 1
            # print(dp)
            # print(index2, index3, index5)
        return dp[n]


if __name__ == '__main__':
    sol = Solution_1()
    res = sol.nthUglyNumber(10)
    print(res)
