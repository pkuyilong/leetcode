# -*- coding: utf-8 -*-
# 2018-12-24 22:52 mayilong

# import os
# import sys
# import numpy as np
# import torch
# import torch.nn as nn
# from torchvision import models
import pdb



def test():
    queue = stack()
    node = 0
    queue.append(node)
    while queue:
        size = len(queue)
        for i in range(size):
            tmp = queue.pop(0)
            if node is tmp.neighbor and visited[node] == 0:
                visited[node] = 1
                queue.append(node)

class Solution:
    def numIslands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        height = len(grid)
        width = len(grid[0])
        queue = []
        island_count = 0
        # visited = [[0 for j in range(width)] for i in range(height)]
        visited = [[0,0,0,0,0,0],
                   [0,0,0,0,0,0],
                   [0,0,0,0,0,0],
                   [0,0,0,0,0,0],
                   [0,0,0,0,0,0]]

        for ii in range(height):
            for jj in range(width):
                # print("have already reached {}-{}".format(ii, jj))
                # print(visited)
                if grid[ii][jj] == 0 and visited[ii][jj] != 1:
                    visited[ii][jj] = 1
                    print("{}-{} unvisited element is 0".format(ii, jj))
                    continue

                if visited[ii][jj] == 1:
                    print("{}-{} has visited".format(ii,jj))
                    continue

                if grid[ii][jj] == 1 and visited[ii][jj] != 1:
                    queue.append([ii, jj])
                    visited[ii][jj] = 1
                    print("{}-{} is unvisited 1 , queue : {} ".format(ii, jj, queue))

                while len(queue) != 0:
                    # pdb.set_trace()
                    tmp = queue[0]
                    i, j = tmp[0], tmp[1]
                    queue = queue[1:]
                    print("remove first element, queue : {}".format(queue))
                        # check four directions

                    # if i > 0 and visited[i-1][j]  != 1:   ## upwards
                    #     if grid[i-1][j] == 1:
                    #         queue.append([i-1, j])
                    #     visited[i-1][j] == 1

                    if j < width and visited[i][j+1] != 1:   ## rightwards
                        print("******** {}".format(visited))
                        visited[i][j+1] == 1
                        print(i, j+1)
                        print("******** {}".format(visited))
                        if grid[i][j+1] == 1:
                            queue.append([i, j+1])
                        print("rightwards is unvisited 1, queue : {}".format(queue))
                        print("now visited is {}".format(visited))


                    if i < height and visited[i+1][j] != 1:  ## downwards
                        print("******** {}".format(visited))
                        visited[i+1][j] == 1
                        print(i, j+1)
                        print("******** {}".format(visited))
                        if grid[i+1][j] == 1:
                            queue.append([i+1, j])
                        print("downwards is unvisited 1, queue : {}".format(queue))
                        print("now visited is {}".format(visited))

                    # if j > 0 and visited[i][j-1] != 1:    ## leftwards
                    #     if grid[i][j-1] == 1:
                    #         queue.append([i, j-1])
                    #     visited[i][j-1] == 1

                visited[ii][jj] = 1
                island_count += 1
        return island_count



if __name__ == "__main__":
    print('*'*80)
    sol = Solution()
    grid = [[0,0,0,0,0,0],
             [0,1,1,1,0,0],
             [0,1,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]

    res = sol.numIslands(grid)
    print(res)
    pass
