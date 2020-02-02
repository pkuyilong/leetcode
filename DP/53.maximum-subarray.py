# 53. 最大子序和
# https://leetcode-cn.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums):
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        max_res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]
            max_res = max(max_res, dp[i])
        return max_res


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution().maxSubArray(nums)
    print(res)
