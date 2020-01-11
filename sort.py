import numpy as np


def partition(nums, start, end):
    if start == end:
        return nums
    i = start
    j = end
    key = nums[start]
    while i < j:
        while i < j and nums[j] >= key:
            j = j - 1
        while i < j and nums[i] <= key:
            i = i + 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i], nums[start] = nums[start], nums[i]
    return i


def quicksort(nums, start, end):
    if start < end:
        mid = partition(nums, start, end)
        quicksort(nums, start, mid - 1)
        quicksort(nums, mid + 1, end)


def partation(nums, start, end):
    if start == end:
        return nums
    i, j = start + 1, end
    key = nums[start]
    while i < j:
        while i < j and nums[j] >= key:
            j -= 1
        while i < j and nums[i] <= key:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[start] = nums[start], nums[i]
    return i


def s(nums, start, end):
    if start >= end:
        return nums
    i = partition(nums, start, end)
    print(i)
    s(nums, start, i)
    s(nums, i + 1, end)
    return nums


if __name__ == '__main__':
    # nums = [np.random.randint(0,30) for _ in range(10)]
    # nums = [17, 28, 5, 6, 12, 21, 27, 25, 1, 23]
    nums = [2]
    # nums = [22, 3, 22, 17, 22, 22, 27]
    # res = partation(nums, 0, len(nums)-1)
    # print(res)
    # quicksort(nums, 0, len(nums) -1 )
    res = s(nums, 0, len(nums) - 1)
    print(res)
