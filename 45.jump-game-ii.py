import sys


class Solution:
    def jump(self, nums):
        if not nums or len(nums) == 1:
            return 0
        dp = [0 for i in range(len(nums))]
        start = 1
        count = 0
        for step in nums:
            for i in range(step):
                if start + i <= len(dp):
                    dp[start + i] = count + 1
            start += step
            count += 1
        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2]
    sol = Solution()
    res = sol.jump(nums)
    print(res)
