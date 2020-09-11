def qs(nums, l, r):
    if l <= r:
        idx = partition(nums, l, r)
        qs(nums, l, idx - 1)
        qs(nums, idx + 1, r)


def partition(nums, l, r):
    pivot = nums[l]
    left = l
    right = r
    while left < right:
        while left < right and nums[right] > pivot:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]

        while left < right and nums[left] <= pivot:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    return left


if __name__ == "__main__":
    # nums = [3, 9, 2, 5, 1, 3, 2]
    nums = [30,24,5,58,18,36,12,42,39]
    qs(nums, 0, len(nums) - 1)
    print(nums)
