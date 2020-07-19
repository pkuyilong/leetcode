
def longestCommonSubstring(s, t):
    """
    ans代表最大公共子串的长度, last_pos记录公共子串的最后的一个位置，目的是为了计算最长公共子串具体是什么
    """
    if s is None or t is None or len(s) == 0 or len(t) == 0:
        return ""
    ans = 0
    last_pos = 0
    dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i+1][j+1] > ans:
                    ans = dp[i+1][j+1]
                    last_pos = i
    return ans, last_pos


# def longest2(s, t):
#     res = 0
#     for i in range(len(s)):
#         for j in range(len(t)):
#             for k in range(1, min(len(s) - (i + 1), len(t) - (j + 1)) + 1):
#                 s1 = s[i: i + k]
#                 t1 = t[j: j + k]
#                 if s1 == t1:
#                     if k > res:
#                         res = k
#                         print("res {}".format(res))
#                         first_pos = i
#     return res, first_pos


if __name__ == '__main__':
    s = "sabced"
    t = 'eeabcs'
    ans, last_pos = longestCommonSubstring(s, t)
    print(ans, last_pos)
    print(s[last_pos + 1 - ans: last_pos + 1])
