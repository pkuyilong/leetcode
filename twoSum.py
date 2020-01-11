# -*- coding: utf-8 -*-
# Copyright © 2018 mayilong <mayilong@mayilong.lan>

"""
使用字典记住下标.
尤其要注意更新的时间问题, 先判断之前的tmp 在之前的
dict 中存不存在. 不然会出现 [3,2,4]  6  返回[0,0]的情况

"""
class Solution(object):
    def twoSum(self, nums, target):
        if nums is None and len(nums) < 2:
            return []
        num_dict = dict()
        for idx, num in enumerate(nums):
            tmp = target - num
            if tmp in num_dict:
                return [num_dict[tmp], idx]
            # update num_dict here
            num_dict.update({num: idx})
        return []


if __name__ == "__main__":
    print("*"*80)
    sol = Solution()
    # nums = [2, 7, 11, 15]
    nums = [3,2,4]
    res = sol.twoSum(nums, 6)
    print(res)
    # test()

    pass
