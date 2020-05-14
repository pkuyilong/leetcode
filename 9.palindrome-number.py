# https://leetcode-cn.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        x = str(x)
        if x.startswith('-') or x.startswith('0') or x.endswith('0'):
            return False
        return x == "".join(list(reversed(x)))


class Solution_1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_list = list()
        while x:
            num_list.append(x % 10)
            x = x // 10
        if len(num_list) == 0:
            return True
        i, j = 0, len(num_list)-1
        while i < j:
            if num_list[i] != num_list[j]:
                return False
            i += 1
            j -= 1
        return True