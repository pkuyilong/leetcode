# 59 spiral-matrix-ii
# https://leetcode-cn.com/problems/spiral-matrix-ii
from pprint import pprint

class Solution(object):
    def generateMatrix(self, n):
        if n <= 0:
            return []

        # 设置一个空矩阵，之后向里填充数据
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        # 设定好右下左上四个方向
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        row, col = len(matrix), len(matrix[0])
        r, c = 0, 0
        idx = 0
        visited = set()
        for i in range(n**2):
            matrix[r][c] = i + 1
            visited.add((r, c))

            # 启用临时变量是因为可能会越界，越界的坐标会被放弃, t代表temp的意思
            tr = r + dx[idx]
            tc = c + dy[idx]
            if 0 <= tr < row and 0 <= tc < col and (tr, tc) not in visited:
                r, c = tr, tc
            else:
                idx = (idx + 1) % 4
                # 这里因为tr tc越界，所以直接使用原来的坐标r c
                r = r + dx[idx]
                c = c + dy[idx]
        return matrix


if __name__ == '__main__':
    sol = Solution()
    res = sol.generateMatrix(3)
    pprint(res)




