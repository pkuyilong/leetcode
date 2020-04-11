import numpy as np


class Solution(object):
    res = list()

    def spiralOrder(self, matrix):
        Solution.res = list()
        self.helper(matrix)
        return Solution.res

    def helper(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return Solution.res
        row = len(matrix)
        col = len(matrix[0])
        if row == 1:
            # 只剩一行 横向打印
            for i in range(col):
                Solution.res.append(matrix[0][i])
            return Solution.res
        if col == 1:
            # 只剩一列 竖向打印
            for i in range(row):
                Solution.res.append(matrix[i][col - 1])
            return Solution.res

        # 从左到右
        for i in range(col):
            Solution.res.append(matrix[0][i])
        # 从上到下
        for i in range(1, row):
            Solution.res.append(matrix[i][col - 1])
        # 从右到左
        for j in range(col - 2, -1, -1):
            Solution.res.append(matrix[row - 1][j])
        # 从下到上
        for j in range(row - 2, 0, -1):
            Solution.res.append(matrix[j][0])
        matrix = np.array(matrix)
        new_matrix = matrix[1: len(matrix) - 1, 1: len(matrix[0]) - 1]
        self.helper(new_matrix)


class Solution_1(object):
    def spiralOrder(self, matrix):
        ans = list()
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return ans

        visited = set()
        row, col = len(matrix), len(matrix[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        c = r = idx = 0
        for _ in range(row * col):
            print(r, c)
            ans.append(matrix[r][c])
            visited.add((r, c))
            temp_r = r + dx[idx]
            temp_c = c + dy[idx]
            if 0 <= temp_r < row and 0 <= temp_c < col and (temp_r, temp_c) not in visited:
                r, c = temp_r, temp_c
            else:
                idx = (idx + 1) % 4
                r = r + dx[idx]
                c = c + dy[idx]
        return ans


if __name__ == '__main__':
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
    arr2 = [[1, 2, 3],
            [5, 6, 7],
            [9, 10, 11]]
    arr3 = [[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]]

    sol = Solution_1()
    res = sol.spiralOrder(arr3)
    print(res)
    # print(Solution.res)
