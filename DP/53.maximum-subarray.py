# 53. 最大子序和
# https://leetcode-cn.com/problems/maximum-subarray/

""" 思路
    dp[i] 代表考虑到第i个位置为止，最大的子序列长度之和
    但是该题目并不是dp数组的最后一个结果为最大值，需要额外使用一个变量来不断更新最大值

    dp[i] = max(dp[i-1],0)  + nums[i]

"""


# 53题解
class Solution_1:
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        max_res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
            max_res = max(max_res, dp[i])
        return max_res


class Solution:
    """
    根据公式 dp[i] = max(dp[i-1], 0) + nums[i]可知，
    dp[i] 只与 dp[i-1]有关系，所以不需要O(n)的空间
    使用cur代替dp[i-1], 使用nxt代替dp[i]即可

    """
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        cur = nums[0]
        nxt = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            cur = nxt
            nxt = cur + nums[i] if cur > 0 else nums[i]
            ans = max(nxt, ans)
        return ans



# 升级版：如果要计算出最大子序列的起始位置， 用这个代码
class Solution_0:
    def maxSubArray(self, nums):
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        max_res = nums[0]

        tmp_pos = 0
        start_pos = 0
        end_pos = 0
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                # 记录当前是从哪个位置开始的，但是从该位置开始的连续子序列不一定是最大的
                tmp_pos = i
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]

            # 如果出现了新的最大值，那么同时更新起始位置
            if dp[i] > max_res:
                max_res = dp[i]
                end_pos = i
                start_pos = tmp_pos
        print(start_pos, end_pos)
        return max_res


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution().maxSubArray(nums)
    print(res)
