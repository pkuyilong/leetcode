import numpy as np


def par(nums, l, r):
    key = nums[r]
    while l < r:

        while l < r and nums[l] < key:
            l += 1
        nums[r] = nums[l]
        print(r)

    while l < r and nums[r] >= key:
        r -= 1
    nums[l] = nums[r]
    print(r)
    nums[l] = key
    return l


def qs(nums, l, r):
    if r < l:
        return
    if nums is None or len(nums) == 1:
        return
    mid = par(nums, l, r)
    print(mid)
    qs(nums, l, mid - 1)
    qs(nums, mid + 1, r)



def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
            print(nums)
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1


if __name__ == '__main__':
    # nums = [5, 2, 2, 7, 5, 4, 1]
    nums = [3, 1, 9, 4, 5, 6, 2]
    print(nums)
    partition(nums, 0, len(nums) - 1)
    print(nums)
    # qs(nums, 0, len(nums) - 1)
    # print(nums)
