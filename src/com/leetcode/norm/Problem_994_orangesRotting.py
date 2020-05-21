from typing import List

class Solution(object):
    def orangesRotting(self, grid):

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        rotlist = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotlist.append([i, j])
        minute = 0
        while rotlist:
            newrotlist = []
            for rotnode in rotlist:
                x0 = rotnode[0]
                y0 = rotnode[1]

                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        newrotlist.append([x, y])
            if not newrotlist:
                break

            rotlist = newrotlist[:]
            minute += 1

        for row in grid:
            for i in row:
                if i == 1:  # 还有新鲜的
                    return -1
        return minute

    def orangesRotting2(self, grid: List[List[int]]) -> int:
        x, y, time = len(grid), len(grid[0]), 0
        locs, stack = [[-1, 0], [0, -1], [0, 1], [1, 0]], []
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 2:
                    stack.append((i, j, 0))
        while stack:
            i, j, time = stack.pop(0)
            for loc in locs:
                loc_i, loc_j = i+loc[0], j+loc[1]
                if 0 <= loc_i < x and 0 <= loc_j < y and grid[loc_i][loc_j] == 1:
                    grid[loc_i][loc_j] = 2
                    stack.append((loc_i, loc_j, time+1))
        for g in grid:
            if 1 in g:
                return -1
        return time

grid = [[2,1,1],[1,1,0],[0,1,1]]
obj = Solution()
res = obj.orangesRotting2(grid)
print(res)