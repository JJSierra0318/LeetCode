'''
I used DSF matrix with recursive calling, if an island is found we increase total
islands found by one and then proceed to eliminate all of the '1's that represent
the current island by replacing the current one with '0' and recursive call the
function for all of its adjacent cells (up, down, right and left)
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res, rows, cols = 0, len(grid), len(grid[0])

        def removeIsland(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            removeIsland(r - 1, c)
            removeIsland(r + 1, c)
            removeIsland(r, c - 1)
            removeIsland(r, c + 1)
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    res += 1
                    removeIsland(i, j)
        return res