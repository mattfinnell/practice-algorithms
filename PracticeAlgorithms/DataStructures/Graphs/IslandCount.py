from collections import deque

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
    
    neighbors = list(get_neighbors(i, j, m, n))

    for a, b in neighbors:
        if not visited[(a, b)] and grid[a][b] == '1':
            depth_first_search(a, b, grid, m, n, visited)

def breadth_first_search(i, j, grid, m, n, visited):
    queue = deque([(i, j)])

    while queue:
        _a, _b = queue.popleft()

        for a, b in get_neighbors(_a, _b, m, n):
            if not visited[(a, b)] and grid[a][b] == '1':
                visited[(a, b)] = True
                queue.append((a, b))

def get_neighbors(i, j, m, n):
    if i > 0: # has a neighbor above
        yield (i - 1, j)

    if j > 0: # has a neighbord to the left
        yield (i , j - 1)

    if i < (m - 1): # has a neighbor below
        yield (i + 1, j)

    if j < (n - 1): # has a neighbor to the right
        yield (i, j + 1)