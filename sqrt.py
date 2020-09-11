# class Solution:
#     def sqrt(self , x ):
#         # write code here
#         if x <= 0:
#             return 0
#         l, r = 0, x
#         while l < r:
#             mid = l + (r - l) // 2
#             if mid * mid == x:
#                 return mid
#             elif mid * mid > x:
#                 r = mid
#             else:
#                 l = mid + 1
#         return l - 1

def search(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
        print(l, r)
    if l == 0:
        return -1
    return l - 1 if nums[l-1] == target else -1




if __name__ == '__main__':
    # sol = Solution()
    # res = sol.sqrt(65)
    # print(res)
    nums = [1, 2, 3, 3, 3, 3, 7, 9, 11]
    res = search(nums, 3)
    print(res)