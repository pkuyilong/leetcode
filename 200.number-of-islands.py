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
        row, col = len(grid), len(grid[0])
        visited = [[False for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, (i, j), visited, row, col)
                    count += 1
        return count

    def dfs(self, grid, start_pos, visited, row, col):
        i, j = start_pos
        # 越界或者已经访问过了, 就直接返回False
        if not self.valid_pos(grid, i, j) or visited[i][j] is True or grid[i][j] == "0":
            return

        visited[i][j] = True

        # 向四个方向继续递归
        y = [1, 0, -1, 0]
        x = [0, 1, 0, -1]
        for idx in range(4):
            i += x[idx]
            j += y[idx]
            self.dfs(grid, (i, j), visited, row, col)
            # note: 这里尤其注意, 要还原i,j的值
            i -= x[idx]
            j -= y[idx]
        return

    def valid_pos(self, grid, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
            return False
        return True


class Solution2(object):
    def numIslands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    self.dfs(grid, i, j, visited)
        return count

    def dfs(self, grid, i, j, visited):
        # 判断边界
        if not self.valid(grid, i, j) or visited[i][j] or grid[i][j] == "0":
            return
        visited[i][j] = True
        self.dfs(grid, i, j + 1, visited)
        self.dfs(grid, i + 1, j, visited)
        self.dfs(grid, i, j - 1, visited)
        self.dfs(grid, i - 1, j, visited)
        return

    def valid(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            return False
        return True


if __name__ == '__main__':
    grids = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    sol = Solution2()
    ans = sol.numIslands(grids)
    print(ans)
