# 342. 4的幂
# https://leetcode-cn.com/problems/power-of-four/


# 4的幂的二进制只有一个是1， 而且是在奇数位上
"""
    4 0b100
   16 0b10000
   64 0b1000000
  256 0b100000000
 1024 0b10000000000
 4096 0b1000000000000
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num & int("10" * 16, base=2) == 0:
            if self.bin_sum(num) == 1:
                return True
        return False

    def bin_sum(self, num):
        sum = 0
        while num > 0:
            sum += num & 1
            num = num >> 1
        return sum


if __name__ == '__main__':
    i = 4
    while i < 10000:
        print("{:5d} {}".format(i, bin(i)))
        i = i << 2
