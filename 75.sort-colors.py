# 荷兰国旗问题
# https://leetcode-cn.com/problems/sort-colors

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        begin = 0
        end = len(nums) - 1
        cur = 0
        # 条件是cur碰到end就要停下，而且是可以相等的
        while cur <= end:
            if nums[cur] == 1:
                cur += 1
            elif nums[cur] == 0:
                nums[cur], nums[begin] = nums[begin], nums[cur]
                cur += 1
                begin += 1
            else:
                nums[cur], nums[end] = nums[end], nums[cur]
                # 这里begin不需要加1，因为换到这里的数字可能是0，也可能是1，需要进一步调整
                end -= 1


# 将数组中的数字以5为轴，会分成两部分
class Solution_0:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        begin = 0
        end = len(nums) - 1
        cur = 0
        # 条件是cur碰到end就要停下，而且是可以相等的
        while cur <= end:
            if nums[cur] == 5:
                cur += 1
            elif nums[cur] < 5:
                nums[cur], nums[begin] = nums[begin], nums[cur]
                cur += 1
                begin += 1
            else:
                nums[cur], nums[end] = nums[end], nums[cur]
                # 这里begin不需要加1，因为换到这里的数字可能是0，也可能是1，需要进一步调整
                end -= 1


if __name__ == '__main__':
    sol = Solution_0()
    nums = [3, 9, 8, 5, 1, 2, 7, 5]
    sol.sortColors(nums)
    print(nums)
