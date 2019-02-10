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