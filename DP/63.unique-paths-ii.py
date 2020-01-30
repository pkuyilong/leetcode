# 63. 不同路径 II
# https://leetcode-cn.com/problems/unique-paths-ii/


""" 主题思路参考 leetcode 62
    区别在于这里增加了障碍，只要在有障碍的地方，将dp中的值设置为0就可以了，
    意味着这一点永远不可以到达，其他的没有改动
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid is None or len(obstacleGrid) == 0 or \
                len(obstacleGrid[0]) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0
        i = 0
        while i < m:
            if obstacleGrid[i][0] != 1:
                obstacleGrid[i][0] = 1
                i += 1
            else:
                break

        while i < m:
            obstacleGrid[i][0] = 0
            i += 1

        j = 1
        while j < n:
            if obstacleGrid[0][j] != 1:
                obstacleGrid[0][j] = 1
                j += 1
            else:
                break

        while j < n:
            obstacleGrid[0][j] = 0
            j += 1
        for item in obstacleGrid:
            print(item)
        print()
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        for item in obstacleGrid:
            print(item)
        return obstacleGrid[m - 1][n - 1]


if __name__ == '__main__':
    # grid = [
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 0]
    # ]
    grid = [[1, 0]]
    res = Solution().uniquePathsWithObstacles(grid)
    print(res)
