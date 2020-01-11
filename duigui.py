import time
from pprint import pprint

memo = [0 for _ in range(200)]

def fib(n):
    """
    递归方式 自上到下
    :param n:
    :return:
    """

    if memo[n] != 0:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
        # return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


# def fib(n):
#     """
#     遍历方式 就是典型的动态规划
#     :param n:
#     :return:
#     """
#     dp = [0 for _ in range(n)]
#     dp[1] = 1
#     dp[2] = 1
#     for i in range(3, n):
#         dp[i] = dp[i-1] + dp[i-2]
#     pprint(dp)

if __name__ == '__main__':
    start = time.time()
    print(fib(199))
    print(time.time() - start)

