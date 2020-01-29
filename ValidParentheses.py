class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 1:
            return False
        stk = []
        d = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in d.values():
                stk.append(ch)
            else:
                if stk and d[ch] == stk[-1]:
                    stk.pop()
                else:
                    return False
        return not stk


if __name__ == "__main__":
    print("*" * 80)
    sol = Solution()
    print(sol.isValid("()"))
