class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid 
        return l
