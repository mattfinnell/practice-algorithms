def neighbors(i, j, m, n):
    if i > 0: # top neighbor
        yield (i - 1, j)
        
    if i < (m - 1): # bottom neighbor
        yield (i + 1, j)
        
    if j > 0: # left neighbor
        yield (i, j - 1)
        
    if j < (n - 1): # right neighbor
        yield (i, j + 1)