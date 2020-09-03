
# https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

"""
利用二分搜索查找插入位置, bisect与bisect.bisect_right是一样的, 都是找到一个位置,从该位置到数组末尾的元素比插入元素的值要大

1. 依次遍历所有的元素
2. 遍历过程中把考虑过的元素驾驭一个临时的有序数组
3. 当新来一个元素的时候, 考虑新元素在临时有序数组中的插入位置
4. 因为bisect_right的缘故, 产生的pos都是大于该插入元素的, 所以比插入元素的大的数量是
length - 1 - pos + 1 = length - pos
5. 将当前元素插入到临时有序数组中, 并保持有序
"""

import bisect
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_list = list()
        count = 0
        for i in range(len(nums)):
            pos = bisect.bisect(nums_list, nums[i])

            count += len(nums_list) - pos
            nums_list.insert(pos, nums[i])

        return count