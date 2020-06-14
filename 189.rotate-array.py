# class Solution(object):
#     def rotate(self, nums, k):
#         if nums is None or len(nums) == 0:
#             return nums
#         k = k % len(nums)
#         nums[:] = nums[-k:] + nums[:len(nums) - k]


class Solution(object):
    def rotate(self, nums, k):
        if nums is None or len(nums) == 0:
            return nums
        k = k % len(nums)
        self.swap(nums, 0, len(nums)-1)
        self.swap(nums, 0, k-1)
        self.swap(nums, k, len(nums)-1)

    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    # nums = [-1, -100, 3, 99]
    sol = Solution()
    sol.rotate(nums, 2)
    print(nums)
