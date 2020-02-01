# 384. 打乱数组
# https://leetcode-cn.com/problems/shuffle-an-array/

import random
from copy import deepcopy


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        res_list = []
        nums_copy = deepcopy(self.nums)
        for i in range(len(self.nums)):
            # 因为要进行交换，所以这里随机数的起点为i
            idx = random.randrange(i, len(nums_copy))
            res_list.append(nums_copy[idx])
            # 数组内部进行交换
            nums_copy[i], nums_copy[idx] = nums_copy[idx], nums_copy[i]
        # print(res_list)
        return res_list


if __name__ == '__main__':
    sol = Solution([1, 2, 3])
    print(sol.shuffle())
    print(sol.shuffle())
    print(sol.shuffle())
