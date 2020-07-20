class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                 left += 1
        # Note left == right的时候，这种情况被跳过了，所以需要我们手动判断一下
        return -1 if nums[left] != target else left