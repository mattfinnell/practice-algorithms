from PracticeAlgorithms.Constants import HOURGLASS_SIZE, HOURGLASS_FILTER

def apply_hourglass_filter(arr, i, j):
    hourglass = []
    for a in range(0, HOURGLASS_SIZE):
        hourglass.append([])

        for b in range(0, HOURGLASS_SIZE):
            hourglass[a].append(HOURGLASS_FILTER[a][b] * arr[i + a][j + b])
    
    return hourglass

def calculate_hourglass_sum(hourglass):
    return sum([item for row in hourglass for item in row])

def hourglass_max_sum(grid):
    m = len(grid) - (HOURGLASS_SIZE - 1)

    hourglasses = []
    for i in range(0, m):
        for j in range(0, m):
            hourglasses.append(apply_hourglass_filter(grid, i, j))
    
    return max([calculate_hourglass_sum(hourglass) for hourglass in hourglasses])