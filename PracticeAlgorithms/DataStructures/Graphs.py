from collections import deque

class Graph(object):
    def __init__(self, adjacency_table):
        self._adjacency_table = adjacency_table
        self.vertices = adjacency_table.keys()

    def disjoint_subgraph_count(self):
        visited = {vertex: False for vertex in self.vertices}

        count = 0
        for vertex in self.vertices:
            if not visited[vertex]:
                count += 1
                self.depth_first_search(vertex)

    def breadth_first_search(self, start, visited=None):
        # init visited table and queue for next node to visit
        if not visited:
            visited = {vertex: False for vertex in self.vertices}

        queue = deque()

        # consider the current state
        visited[start] = True
        queue.append(start)

        while queue:
            current_vertex = queue.popleft()

            yield current_vertex

            for next_vertex in self._adjacency_table[current_vertex]:
                if not visited[next_vertex]:
                    visited[next_vertex] = True
                    queue.append(next_vertex)

    def depth_first_search(self, start, visited=None):
        if not visited:
            visited = { vertex: False for vertex in self.vertices }

        traversal = deque()

        self._depth_first_search(start, visited, traversal)

        return traversal

    def _depth_first_search(self, current, visited, traversal):
        visited[current] = True

        traversal.append(current)

        for next_vertex in self._adjacency_table[current]:
            if not visited[next_vertex]: 
                self._depth_first_search(next_vertex, visited, traversal)

def build_adjacency_table(adjacency_matrix):
    table = {}
    for i, adjacents in enumerate(adjacency_matrix):
        table[i] = []

        for j, adjacent in enumerate(adjacents):
            if j != i and adjacent == 1:
                table[i].append(j)
    
    return table

def get_neighbors(i, j, m, n):
    if i > 0: # has a neighbor above
        yield (i - 1, j)

    if j > 0: # has a neighbord to the left
        yield (i , j - 1)

    if i < (m - 1): # has a neighbor below
        yield (i + 1, j)

    if j < (n - 1): # has a neighbor to the right
        yield (i, j + 1)


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