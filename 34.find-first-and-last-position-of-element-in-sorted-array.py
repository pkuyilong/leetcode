class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        print(l, r)
        if l == len(nums):
            return -1
        if nums[l] == target:
            lres = l
        else:
            lres = -1
        print(lres)

        # l, r = 0, len(nums)
        # while l < r:
        #     mid = (l + r) // 2
        #     if nums[mid] <= target:
        #         l = mid + 1
        #     else:
        #         r = mid
        # if l != 0 and nums[l - 1] == target:
        #     rres = l - 1
        # else:
        #     rres = -1
        # return [lres, rres]

"""
[l, r)
[l, l)   r一直往左移动

[r, r)
"""
if __name__ == '__main__':
    nums = [2, 2]
    sol = Solution()
    res = sol.searchRange(nums, 10)
    print(res)
