# 198. 打家劫舍
# https://leetcode-cn.com/problems/house-robber/


class Solution:
    def rob(self, nums):
        """
        dp 中存放的是当前位置中 ##不触发警报## 的情况下能获取的最大值

        当到了一个新的位置i，只需不抢劫i-1的位置，报警就不会触发
        因为之前的那个位置既然已经保存了 ##不触发警报## 的最大值，
        所以只需要往前遍历找到最大值相加即可
        """
        if nums is None or len(nums) == 0:
            return 0

        dp = [nums[i] for i in range(len(nums))]
        ans = nums[0]

        for i in range(1, len(nums)):
            max_val = 0
            # 为了避免触发警报，这里排除了i之前第一个位置(也就是i-1)

            for j in range(i - 1):
                max_val = max(max_val, dp[j])
            dp[i] = nums[i] + max_val
            ans = max(dp[i], ans)
        return ans


class Solution:
    def rob(self, nums):
        """
        dp 中存放的是当前位置中 ##不触发警报## 的情况下能获取的最大值

        当到了一个新的位置i，只需不抢劫i-1的位置，报警就不会触发
        其实可以不用遍历，因为全是非负正数，是单调上升的

        """
        if nums is None or len(nums) == 0:
            return 0
        dp = [0 for i in range(len(nums))]

        #  注意第一个和第二个元素的初始化， 要考虑数组越界的问题
        dp[0] = nums[0]
        if len(nums) >= 2:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums) - 1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    sol = Solution()
    res = sol.rob(nums)
    print(res)
