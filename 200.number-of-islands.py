class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 边界条件判断
        if grid is None or len(grid) == 0 or len(grid[0][0]) == 0:
            return 0

        count = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, (i, j), visited, m, n)
                    count += 1
        return count

    def dfs(self, grid, start_pos, visited, row, col):
        i, j = start_pos

        # 越界或者已经访问过了, 就直接返回False
        if i < 0 or i > row - 1 or j < 0 or j > col - 1:
            return
        if visited[i][j] is True:
            return
        if grid[i][j] == "0":
            return

        visited[i][j] = True

        # 向四个方向继续递归
        y = [1, 0, -1, 0]
        x = [0, 1, 0, -1]
        for idx in range(4):
            i += x[idx]
            j += y[idx]
            self.dfs(grid, (i, j), visited, row, col)
            i -= x[idx]
            j -= y[idx]
        return


if __name__ == '__main__':
    grids = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    sol = Solution()
    ans = sol.numIslands(grids)
    print(ans)
