# 64. 最小路径和
# https://leetcode-cn.com/problems/minimum-path-sum/

"""

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

"""

class Solution:
    """ 思路
        1. 就是一个公式，到达当前位置只有两种途径
            1.1 从上边过来
            1.2 从左边过来
            1.3 grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

    """
    def minPathSum(self, grid):
        if grid is None:
            return 0
        if len(grid) == 1:
            return sum(grid[0])
        if len(grid[0]) == 1:
            return sum([tmp_list[0] for tmp_list in grid])

        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[m - 1][n - 1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    sol = Solution()
    res = sol.minPathSum(grid)
    print(res)
