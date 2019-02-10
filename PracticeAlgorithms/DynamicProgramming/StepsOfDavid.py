def step_perms(n):
    cache = {
        0: 0,
        1: 1,
        2: 2,
        3: 4,
    }

    return _step_perms(n, cache)

def _step_perms(n, cache):
    if n in cache:
        return cache[n]
    
    cache[n] = sum((_step_perms(i, cache) for i in range(n - 3, n)))

    return cache[n] 