# class Solution:
#     def searchInsert(self, nums, target):
#         if not nums or len(nums) == 0:
#             return 0
#         l, r = 0, len(nums)
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid
#         return l


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            # 如果该数字小于target 那么这个值一定要别排除掉，左边界向右移动
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    res = sol.searchInsert(nums, 8)
    print(res)
