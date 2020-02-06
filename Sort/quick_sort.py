# 快速排序
""" 思路
    1. 找出一个枢纽节点key
    2. 将数组划分成左右两部分数组，左边数组中的值都比枢纽节点的值小，右边数组中的节点的值都要key比枢纽节点key的值大
    3. 对左边数组进行求解，返回排序后的数组 left_arr
    4. 对右边数据进行求解，返回排序后的数组 right_arr
    5. 将左边数组和右边数组以及枢纽节点进行拼接

"""
class Solution():
    def quick_sort(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        less = list()
        more = list()
        mid = list()
        key = nums[0]
        for num in nums:
            if num < key:
                less.append(num)
            elif num > key:
                more.append(num)
            else:
                mid.append(num)
        left_arr = self.quick_sort(less)
        right_arr = self.quick_sort(more)
        return left_arr + mid + right_arr


if __name__ == '__main__':
    nums = [1, 2, 1, 0, 3, 9, 2]
    res = Solution().quick_sort(nums)
    print(res)


