# 279. 完全平方数
# https://leetcode-cn.com/problems/perfect-squares/

import math
import sys

"""
   ___ ___   __| (_)_ __   __ _ 
  / __/ _ \ / _` | | '_ \ / _` |
 | (_| (_) | (_| | | | | | (_| |
  \___\___/ \__,_|_|_| |_|\__, |
                          |___/ 
"""
class Solution:
    """
    这道题目跟最长递增子序列很相似，都是从当前位置查找之前的位置。

    动态规划： i为当前元素，然后考虑小于当前元素的若干个数字的平方
    dp[i] 表示数字i使用的最小平方数
    dp[i] = min(   dp[i - j*j] + 1,      dp[i]   )
            当前位置之前的元素，找个最小的   当前元素，由于是一个遍历，该值一直是记录之前最小的

     仔细考虑一下，dp的公式类似于一个循环中查找最小值的逻辑
    min_val = min(min_val, cur_val)
    """

    def numSquares(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            # 每次最坏的结果就是i，就是每个数字由i个1组成
            # 这样就避免了使用最大值填充dp数组了
            dp[i] = i

            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i - j * j] + 1, dp[i])
        return dp[n]


from queue import Queue
import math

class Solution_1:
    def numSquares(self, n):
        """
        BFS 需要进行剪枝，备忘录法，如果已经计算过了，就不要再计算了
        :param n:
        :return:
        """
        q = Queue()
        q.put(n)
        visited = set()
        visited.add(n)
        level = 1

        while not q.empty():
            # 遍历每一层
            for _ in range(q.qsize()):
                node = q.get()
                # 依次减去小于node的平方和，构造出下一层的值
                for i in range(1, int(math.sqrt(node)) + 1):
                    tmp = node - i * i
                    # 如果已经计算过了， 就跳过
                    if tmp in visited:
                        continue
                    if tmp == 0:
                        return level

                    if tmp > 0:
                        q.put(tmp)
                        visited.add(tmp)
            level = level + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    res = sol.numSquares(12)
    print(res)
