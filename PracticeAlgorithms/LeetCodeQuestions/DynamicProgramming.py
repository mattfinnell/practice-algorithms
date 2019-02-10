def max_subarray_skip_sum(Arr):
    return recursive_memoized(Arr)

def recursive(Arr):
    n = len(Arr)
    if n == 0: return 0 
    if n == 1: return Arr[0]
    if n == 2: return max(Arr)
    if n == 3: return max(Arr[0] + Arr[2], Arr[1])

    leftmost = recursive(Arr[:-2])
    left = recursive(Arr[:-1])
    middle = recursive(Arr[1:-1])
    right = recursive(Arr[1:])

    return max(leftmost + Arr[-1], left, middle, right)

def recursive_indexed(Arr):
    n = len(Arr)

    if n == 0:
        return 0 

    return _recursive_indexed(Arr, 0, n - 1)

def _recursive_indexed(Arr, i, j):
    n = (j - i) + 1

    if n == 1: return Arr[i]
    if n == 2: return max(Arr[i], Arr[j])
    if n == 3: return max(Arr[i] + Arr[i + 2], Arr[i + 1])

    leftmost = _recursive_indexed(Arr, i, j - 2)
    left = _recursive_indexed(Arr, i, j - 1)
    middle = _recursive_indexed(Arr, i + 1, j - 1)
    right = _recursive_indexed(Arr, i + 1, j)

    return max(leftmost + Arr[j], left, middle, right)

def recursive_memoized(Arr):
    n = len(Arr)

    if n == 0:
        return 0 

    cache = {}
    return _recursive_memoized(Arr, 0, n - 1, cache)

def _recursive_memoized(Arr, i, j, cache):
    key = f"{i}:{j}"

    if key in cache:
        return cache[key]

    n = (j - i) + 1

    # Base Cases
    if n == 1: cache[key] = Arr[i]
    elif n == 2: cache[key] = max(Arr[i], Arr[j])
    elif n == 3: cache[key] = max(Arr[i] + Arr[i + 2], Arr[i + 1])

    # Recursive Case
    else: 
        leftmost = _recursive_memoized(Arr, i, j - 2, cache)
        left = _recursive_memoized(Arr, i, j - 1, cache)
        middle = _recursive_memoized(Arr, i + 1, j - 1, cache)
        right = _recursive_memoized(Arr, i + 1, j, cache)

        cache[key] = max(leftmost + Arr[j], left, middle, right)
    
    return cache[key]

def iterative(Arr):
    n = len(Arr)

    if n == 0: return 0
    if n == 1: return Arr[0]
    if n == 2: return max(Arr)
    if n == 3: return max(Arr[0] + Arr[2], Arr[1])
    
    #init 
    i = 0
    if (Arr[0] + Arr[2]) < (Arr[1] + Arr[3]):
        i = 1

    value = Arr[i]
    while i + 3 < n:
        if Arr[i + 2] < Arr[i + 3]:
            i += 3

        else : 
            i += 2

        value += Arr[i]

    return value 
