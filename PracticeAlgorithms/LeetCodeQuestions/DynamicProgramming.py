def max_subarray_skip_sum(Arr):
    return recursive(Arr)

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
