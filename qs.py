nums = [5, 21, 9, 12, 3, 7, 12, 17, 6, 21]


def quick_sort(nums, l, r):
    if l >= r:
        return
    idx = partition(nums, l, r)
    quick_sort(nums, l, idx - 1)
    quick_sort(nums, idx + 1, r)
    return


def partition(nums, l, r):
    key = nums[l]
    while l < r:
        while l < r and nums[r] > key:
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]

        while l < r and nums[l] <= key:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[l] = key
    return l


if __name__ == '__main__':
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
