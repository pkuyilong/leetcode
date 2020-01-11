# 204. 计数质数
# https://leetcode-cn.com/problems/count-primes/
# 统计所有小于非负整数 n 的质数的数量。

import math

class Solution_0:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        if n == 3:
            return 1

        dp = [0 for i in range(n)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1

        prime_nums = set()
        prime_nums.add(2)
        for num in range(3, n):
            if self.is_prime_num(num, prime_nums):
                dp[num] = dp[num - 1] + 1
                prime_nums.add(num)
            else:
                dp[num] = dp[num - 1]
        return dp[n-1]


    def is_prime_num(self, num, prime_nums):
        for prime_num in prime_nums:
            if num % prime_num == 0:
                return False
        return True

class Solution:
    def countPrimes(self, n):
        """
        思路和以上方法一样，只不过是进行了逆向操作，先把不是素数的找出来了，那么剩下的自然就是素数
        """
        if n <= 2:
            return 0
        arr = [True for i in range(n)]
        for num in range(2, n):
            if arr[num]:
                num_multiple = 2 * num
                # 把num的倍数去掉，因为他们是非质数
                while num_multiple < n:
                    arr[num_multiple] = False
                    num_multiple += num

        # 统计质数个数
        count = 0
        for num in range(2, n):
            if arr[num] == True:
                count += 1
        return count


if __name__ == '__main__':
   sol = Solution()
   res = sol.countPrimes(3)
   print(res)

