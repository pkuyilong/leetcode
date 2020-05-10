# https://leetcode-cn.com/problems/maximal-square/

"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""


class Solution(object):
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_res = 0
        matrix = [[int(matrix[j][i]) for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        # 主要考虑他的左上角/左边/右边，一开始没想到
                        matrix[i][j] = min(matrix[i - 1][j - 1],
                                           matrix[i - 1][j],
                                           matrix[i][j - 1]) + 1
                    max_res = max(max_res, matrix[i][j])

        return max_res ** 2


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    sol = Solution()
    res = sol.maximalSquare(matrix)
    print(res)
