

class Solution(object):
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ""
        max_len = 0
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                res = self.check(s, i, j)
                print(i, j, res)
                if res:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        ans = s[i: j + 1]
        return ans

    def check(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    s = "cbbd"
    sol = Solution()
    res = sol.longestPalindrome(s)
    print(res)