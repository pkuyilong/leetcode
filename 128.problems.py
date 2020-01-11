# 128. 最长连续序列
# https://leetcode-cn.com/problems/longest-consecutive-sequence


from pprint import pprint


# 时间复杂度 O(n^2)
# 空间复杂度O(n), 因为使用到了set. 如果不使用set，时间复杂度变为O(n^3)
class Solution1_0:
    def longestConsecutive(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        res = 0
        nums_set = set(nums)
        for num in nums:
            cur = num
            count = 1
            # 这里最大遍历次数是len(nums)
            while cur + 1 in nums_set:
                cur += 1
                count += 1
            res = max(res, count)
        return res


# 空间复杂度仍然是O(n^2)
# 时间复杂度仍然是O(n)
class Solution1_1:
    def longestConsecutive(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        res = 0
        nums_set = set(nums)
        for num in nums:
            left_num = num - 1
            if left_num not in nums_set:
                # 说明num是某一个递增数字序列的第一个数字
                cur = num
                count = 1

                # 这里最大遍历次数是len(nums)
                while cur + 1 in nums_set:
                    cur += 1
                    count += 1
                res = max(res, count)
        return res


class Solution2_0:
    def longestConsecutive(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        nums.sort()
        res = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                else:
                    # 这样会减少res的跟新次数，但是返回结果应该是max(res, count)
                    res = max(count, res)
                    count = 1
        # 注意返回结果
        return max(res, count)


class Solution2_1:
    def longestConsecutive(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        nums.sort()
        res = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                    # 一有数据就马上更新
                    res = max(count, res)
                else:
                    count = 1
        return res


class Solution(object):
    def longestConsecutive(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        d = {}
        res = 1
        for num in nums:
            if num not in d.keys():
                left = d.get(num - 1, 0)
                right = d.get(num + 1, 0)
                d[num] = left + right + 1
                res = max(res, d[num])

                # 很巧妙
                d[num-left] = d[num]
                d[num+right] = d[num]

        pprint(d)
        return res


if __name__ == '__main__':
    # nums = [100, 4, 200, 1, 3, 2]
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    sol = Solution()
    print(sol.longestConsecutive(nums))
