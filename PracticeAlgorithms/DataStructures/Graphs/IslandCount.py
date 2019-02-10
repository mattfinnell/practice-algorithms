from collections import deque
from .Utilities import neighbors

class Solution:
    def numIslands(self, grid):
        m = len(grid)
        if m == 0: # Base case: empty grid
            return 0

        n = len(grid[0])
        
        visited = {(i, j) : False for i in range(m) for j in range(n)}
        
        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[(i, j)] and grid[i][j] == '1':
                    breadth_first_search(i, j, grid, m, n, visited)
                    count += 1
                    
        return count

def depth_first_search(i, j, grid, m, n, visited):
    visited[(i, j)] = True
    
    for a, b in neighbors(i, j, m, n):
        if not visited[(a, b)] and grid[a][b] == '1':
            depth_first_search(a, b, grid, m, n, visited)

def breadth_first_search(i, j, grid, m, n, visited):
    queue = deque([(i, j)])

    while queue:
        _a, _b = queue.popleft()

        for a, b in neighbors(_a, _b, m, n):
            if not visited[(a, b)] and grid[a][b] == '1':
                visited[(a, b)] = True
                queue.append((a, b))