# https://leetcode-cn.com/problems/plus-one/
from typing import List

"""
1. 首先检查输入有效性
2. 考虑末尾的数字小于9的情况
3. 考虑末尾数据等于9的情况,此时会产生进位
    1. 因为加1的操作只会在最后一位上进行加1, 需要单独判断. 其他的位置都是值考虑进位就可以
    2. 然后处理和为10 和 小于10的情况
    
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits is None or len(digits) == 0:
            return digits
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits

        flag = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                num = digits[i] + 1
            else:
                num = digits[i] + flag
            # 如果和为10
            if num == 10:
                if i != 0:
                    digits[i] = 0
                    flag = 1
                else:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return digits
            # 和小于10
            else:
                digits[i] = num
                return digits
