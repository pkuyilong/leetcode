# reverse-integer


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        num_list = list()
        x = abs(x)
        while x:
            num_list.append(x % 10)
            x = x // 10
        i = 0
        while i < len(num_list):
            if num_list[i] != 0:
                break
            i += 1
        ans = 0
        while i < len(num_list):
            ans = ans * 10 + num_list[i]
            i += 1
        ans = ans * sign
        if ans < -2 ** 31 or ans > 2 ** 31 - 1:
            return 0
        return ans
