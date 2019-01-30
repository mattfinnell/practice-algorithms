from itertools import chain

def robot_path(grid):
    start_row = start_column =0
    end_row = len(grid) - 1 
    end_column = len(grid[0]) - 1 

    result = list(_robot_path(grid, start_row, start_column, end_row, end_column))

    return result

def _robot_path(grid, i, j, end_row, end_column):
    current_location = (i, j)

    # Base Case : Reached the end locaiton
    if i == end_row and j == end_column:
        yield current_location

    # recurse
    else:
        current_location = iter([current_location])

        if i < end_row and grid[i + 1][j]:
            yield from chain(current_location, _robot_path(grid, i + 1, j, end_row, end_column))
        
        elif j < end_column and grid[i][j + 1]:
            yield from chain(current_location, _robot_path(grid, i, j + 1, end_row, end_column))