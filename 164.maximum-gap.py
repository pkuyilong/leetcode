

# https://leetcode-cn.com/problems/maximum-gap
# https://leetcode-cn.com/problems/maximum-gap/solution/zui-da-jian-ju-by-leetcode/
import sys


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1])

        # 计算最大最小值
        min_val = nums[0]
        max_val = nums[0]
        for num in nums:
            max_val = max(max_val, num)
            min_val = min(min_val, num)
        # 计算间距/ 计算桶
        interval = max(1, (max_val - min_val) // (len(nums) - 1))
        bucket_num =  (max_val - min_val) // interval + 1
        buckets = [[sys.maxsize, 0] for _ in range(bucket_num)]

        # 将数据放入桶中
        used_set = set()
        for num in nums:
            idx = (num - min_val) // interval
            used_set.add(idx)
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        # 遍历所有的数据, 计算相邻桶的最大最小值
        max_interval = 0
        prev = min_val
        for i in range(len(buckets)):
            if i in used_set:
                max_interval = max(max_interval, buckets[i][0] - prev)
                prev = buckets[i][1]
        return max_interval

if __name__ == '__main__':
    nums = [1, 3, 100]
    sol = Solution()
    res = sol.maximumGap(nums)
    print(res)
