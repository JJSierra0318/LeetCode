'''
Used matrix BSF where rotten will represent a set with the oranges
which have been rotten, and fresh so that I know at the end if every
orange got rotten or not. After the fact I realized a set() for fresh
wasn't necessary as just keeping count would suffice
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        rotten = set()
        fresh = set()
        queue = deque()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    rotten.add((i, j))
                    queue.append((i, j, 0))
        
        if not fresh:
            return 0

        while queue:
            r, c, minute = queue.popleft()
            if min(r, c) < 0 or r == rows or c == cols or not grid[r][c]:
                continue
            if grid[r][c] == 1:
                fresh.remove((r, c))
                grid[r][c] = 2
            if not fresh:
                return minute

            for dr, dc in directions:
                if (r + dr, c + dc) not in rotten:
                    queue.append((r + dr, c + dc, minute + 1))
                    rotten.add((r + dr, c + dc))

        return -1