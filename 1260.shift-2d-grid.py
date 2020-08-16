#  https://leetcode-cn.com/problems/shift-2d-grid/

import numpy as np

"""
按照按照旋转的逻辑写代码就可以, 主要是使用numpy会使得操作更加便捷
"""

class Solution(object):
    def shiftGrid(self, grid, k):
        grid = np.array(grid)
        for i in range(k):
            self.move(grid)
        return grid.tolist()

    def move(self, grid):
        """
        数组转一次后的结果, 相当于k==1
        """
        m, n = grid.shape
        # 保留最后一列
        last_col = grid[:, n - 1:n].copy()

        # 其他列水平右移
        grid[:, 1:] = grid[:, 0:n - 1]

        # 将最后一列的最后一个放到开头, 其他的依次向下移动
        bottom = last_col[m-1][0]
        last_col[1: m, :] = last_col[0:m-1, :]
        last_col[0][0] = bottom

        # 写会到第一列
        grid[:, 0] = last_col[:, 0]