# 322. 零钱兑换
# https://leetcode-cn.com/problems/coin-change/


import sys
import time


class Solution_0:
    def coinChange(self, coins, amount):
        """
        依次计算从1到amount的值, 因为后面取的值会依赖前面的值
        """
        if amount == 0:
            return 0

        # 初始化dp
        dp = [0 for i in range(amount + 1)]

        for i in range(1, amount + 1):
            # 初始tmp非常重要，因为要求最小值，所以设置tmp为python能表示的最大值
            tmp = sys.maxsize

            for j in range(len(coins)):
                # 如果当前值恰好是备选硬币的值，在该位置设置为1
                if i == coins[j]:
                    dp[i] = 1
                    break
                # 当前要求的值肯定是之前的某个数值加上现在的coins中某个硬币的值得到的，
                # 所以依次测试coin的值，查找使用哪个硬币会得到更小的值
                elif i >= coins[j]:
                    if dp[i - coins[j]] != 0:
                        tmp = min(tmp, dp[i - coins[j]] + 1)
                        dp[i] = tmp
        return dp[amount] if dp[amount] != 0 else -1


class Solution_1:
    def coinChange(self, coins, amount):
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0
        # 以下代码有风险， coins的值可能直接大约amount的值， 例如coins=【2】， amount = 1
        # for coin in coins:
        #     dp[coin] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                dp[i] = min(dp[i], self.get_dp(dp, i-coin) + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1


    def get_dp(self, dp, i):
        if i >= 0:
            return dp[i]
        else:
            return sys.maxsize


class Solution_2:
    def coinChange(self, coins, amount):
        memo = [sys.maxsize for _ in range(amount + 1)]
        memo[0] = 0
        self.coinChangeHelper(memo, coins, amount)
        return memo[amount] if memo[amount] != sys.maxsize else -1

    def coinChangeHelper(self, memo, coins, amount):
        if amount < 0:
            return sys.maxsize

        if memo[amount] != sys.maxsize:
            return memo[amount]

        for coin in coins:
            memo[amount] = min(memo[amount],
                               self.coinChangeHelper(memo, coins, amount - coin) + 1)
        return memo[amount] if memo[amount] != sys.maxsize else sys.maxsize


class Solution_3():
    def coinChange(self, coins, amount):
        """
        BFS
        """
        self.ans = sys.maxsize
        self.coinChangeHelper(coins, amount, 0, self.ans)
        return self.ans if self.ans != sys.maxsize else -1

    def coinChangeHelper(self, coins, amount, depth, ans):
        if amount < 0:
            return
        if amount == 0:
            self.ans = min(self.ans, depth)
            print(self.ans)
            return
        for coin in coins:
            self.coinChangeHelper(coins,
                                  amount - coin,
                                  depth + 1,
                                  self.ans)


from queue import Queue

class Solution():
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        min_level = sys.maxsize
        q = Queue()
        q.put(amount)
        level = 0
        visited = set()

        while not q.empty():
            # 直接对队列中的元素进行处理
            for _ in range(q.qsize()):
                node = q.get()
                if node == 0:
                    min_level = min(min_level, level)
                    return min_level

                for coin in coins:
                    if node - coin in visited:
                        continue
                    if node - coin >= 0:
                        q.put(node - coin)
                        # 此算法的精髓，对节点进行剪枝
                        visited.add(node - coin)
            level = level + 1
        return min_level if min_level != sys.maxsize else -1


if __name__ == '__main__':
    start = time.time()
    coins = [1, 2, 5]
    amount = 63
    sol = Solution()
    res = sol.coinChange(coins, amount)
    print(res)
    print(time.time() - start)
