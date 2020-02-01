# 139. 单词拆分
# https://leetcode-cn.com/problems/word-break/

"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

""" 思路
    动态规划题目通常都是dp[i]与dp[i-1]、dp[i-2]之间的关系，但是此题又稍微扩充了一点
    dp[i]与dp[i-len(word)-1]之间的关系，相对来说也比较纯粹
    
    dp[i]表示到第i个字符位置，是否可以用wordDict中的单词拼凑出来
    0代表无法拼凑出来，1代表可以拼凑出来
    
    如果dp[i-len(word)]为1，也就是说当前抠出来的这个单词在wordDict中，
    而且之前字符串是有效的，那么dp[i]也就是有效的
    
    dp[i] =  1   if  截取出来的单词在wordDict中 and dp[i-len(截取出来的单词)] == 1
          =  0   else
"""
import sys
class Solution:
    def wordBreak(self, s, wordDict):
        if not s or len(s) == 0:
            return False

        len_word = {}
        min_len, max_len = sys.maxsize, 0
        for word in wordDict:
            if len(word) not in len_word.keys():
                len_word[len(word)] = {word}
            else:
                len_word[len(word)].add(word)
            min_len = min(min_len, len(word))
            max_len = max(max_len, len(word))
        # print(len_word)
        print(min_len, max_len)

        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        for i in range(len(s)):
            j = i
            while j >= 0:
                clipped_len = i - j + 1
                if clipped_len < min_len or clipped_len > max_len:
                    j -= 1
                    continue

                # 截取出来的长度
                tmp = s[j:i+1]
                if len(tmp) in len_word.keys():
                    if tmp in len_word[len(tmp)] and dp[j] == 1:
                        dp[i+1] = 1
                        break
                j -= 1
        # print(dp)
        return dp[len(s)]


if __name__ == '__main__':
    # wordDict = {"leet", "code", "etc"}
    wordDict = {"apple", "pen"}
    word = "applepenapple"
    res = Solution().wordBreak(word, wordDict)
    print(res)

