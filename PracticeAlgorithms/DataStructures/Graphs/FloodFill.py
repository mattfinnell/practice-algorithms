from .Utilities import neighbors
from collections import deque

def flood_fill_dfs(image, i, j, new_color):
    m, n, old_color, visited = _init(image, i, j)

    return _flood_fill_dfs(image, i, j, m, n, old_color, new_color, visited)

def flood_fill_bfs(image, i, j, new_color):
    m, n, old_color, visited = _init(image, i, j)

    return _flood_fill_bfs(image, i, j, m, n, old_color, new_color, visited)

# 64ms and 6.8MB on leetcode
def _flood_fill_dfs(image, i, j, m, n, old_color, new_color, visited):
    visited[(i, j)] = True
    image[i][j] = new_color
    
    for a, b in neighbors(i, j, m, n):
        if image[a][b] == old_color and not visited[(a, b)]:
            _flood_fill_dfs(image, a, b, m, n, old_color, new_color, visited)
    
    return image

def _flood_fill_bfs(image, i, j, m, n, old_color, new_color, visited):
    queue = deque([(i, j)])
    visited[(i, j)] = True

    while queue:
        _a, _b = queue.popleft()
        visited[(_a, _b)] = True
        image[_a][_b] = new_color

        for a, b in neighbors(_a, _b, m, n):
            if not visited[(a, b)] and image[a][b] == old_color:
                queue.append((a, b))
    
    return image

def _init(image, i, j):
    m = len(image)
    n = len(image[0])
    old_color = image[i][j]
    visited = {(i, j): False for i in range(m) for j in range(n)}

    return (m, n, old_color, visited)