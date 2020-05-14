# https://leetcode-cn.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        x = str(x)
        if x.startswith('-') or x.startswith('0') or x.endswith('0'):
            return False
        return x == "".join(list(reversed(x)))
