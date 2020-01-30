# 72. 编辑距离
# https://leetcode-cn.com/problems/edit-distance/

"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')



字符的问题，一般都是动态规划问题，而且一般与dp[i][j], dp[i-1][j], dp[i][j-1]有关


dp[i][j]表示当word1在i位置， word2在j位置时，最小的改动次数
1. 如果字符不同：
    1.1 可以在第一个单词后边插入一个字符
        dp[i][j-1]
    1.2 可以在第一个单词中删除一个字符
        dp[i-1][j]
    1.3 可以将第一个单词的i位置字符换成第二个单词j位置的字符
        dp[i-1][j-1]
    总的公式就是  dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

2. 如果字符相同：
    dp[i][j] = dp[i-1][j-1]
"""


class Solution_0:
    def minDistance(self, word1, word2):
        if word1 is None or word2 is None:
            return 0
        w1_len, w2_len = len(word1), len(word2)
        if w1_len == 0 or w2_len == 0:
            return w1_len if w2_len == 0 else w2_len
        dp = [[0 for i in range(w2_len + 1)] for j in range(w1_len + 1)]
        for i in range(w2_len + 1):
            dp[0][i] = i
        for i in range(w1_len + 1):
            dp[i][0] = i
        for i in range(1, w1_len + 1):
            for j in range(1, w2_len + 1):
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1],
                                   dp[i][j - 1],
                                   dp[i - 1][j]) + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        for item in dp:
            print(item)
        return dp[w1_len][w2_len]


class Solution:
    def minDistance(self, word1, word2):
        if word1 is None or word2 is None:
            return 0
        w1_len, w2_len = len(word1), len(word2)
        if w1_len == 0 or w2_len == 0:
            return w1_len if w2_len == 0 else w2_len

        dp = [i for i in range(w2_len + 1)]
        print(dp)
        for i in range(1, w1_len+1):
            tmp = dp[0]
            dp[0] = i
            for j in range(1, w2_len+1):
                # 先保存下来dp之前的数值
                pre = tmp
                # 因为马上就要更新dp[j]，所以提前保留下来
                tmp = dp[j]
                if word1[i-1] != word2[j-1]:
                    dp[j] = min(min(dp[j-1], dp[j]), pre) + 1
                else:
                    dp[j] = pre
            print(dp)
        return dp[w2_len]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    sol = Solution_0()
    res = sol.minDistance(word1, word2)
    print(res)
