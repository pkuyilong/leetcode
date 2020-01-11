# 152. 乘积最大子序列
# https://leetcode-cn.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        # 不断保存到当前值的最小值tmp_min和最大值tmp_max
        # 之后的最大值基于tmp_min tmp_max进行计算
        tmp_min = nums[0]
        tmp_max = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            # 防止变量被覆盖, 这才是重点
            tmp_min_copy = tmp_min
            tmp_max_copy = tmp_max

            # 要考虑nums[i]的情况，因为数组中可能有0
            tmp_min = min(tmp_min_copy * nums[i], tmp_max_copy * nums[i], nums[i])
            tmp_max = max(tmp_min_copy * nums[i], tmp_max_copy * nums[i], nums[i])
            ans = max(tmp_max, ans)
        return ans


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    sol = Solution()
    res = sol.maxProduct(nums)
    print(res)
