def merge(nums, l, r):
    if l == r:
        return [nums[l]]
    mid = (l + r) // 2
    left = merge(nums, l, mid)
    right = merge(nums, mid+1, r)
    merged_nums = process(left, right)
    return merged_nums


def process(left, right):
    result = list()
    l1 = len(left)
    l2 = len(right)
    i1 = 0
    i2 = 0
    while i1 < l1 and i2 < l2:
        if left[i1] < right[i2]:
            result.append(left[i1])
            i1 += 1
        else:
            result.append(right[i2])
            i2 += 1

    if i1 == l1 and i2 == l2:
        return result
    elif i1 == l1:
        while i2 < l2:
            result.append(right[i2])
            i2 += 1
    else:
        while i1 < l1:
            result.append(left[i1])
            i1 += 1
    return result


if __name__ == '__main__':
    nums = [3, 9, 4, 8, 1, 2, 5, 10, 83, 38, 101, 115, 73]
    res = merge(nums, 0, len(nums) - 1)
    print(res)
    # n1 = [1, 4, 10]
    # n2 = [3 ,5, 9, 11]
    # res = process(n1, n2)
    # print(res)
