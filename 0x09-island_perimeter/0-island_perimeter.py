#!/usr/bin/python3
"""island perimeter"""


def island_perimeter(grid):
    """return the perimeter
    grid: input
    """
    perimeter = 0

    row = len(grid)
    col = len(grid[0])

    for q in range(row):
        for w in range(col):
            if grid[q][w] == 1:  # theres a land
                perimeter += 4  # for all corners of the land

                if q > 0 and grid[q - 1][w] == 1:  # check above
                    perimeter -= 1  # remove the corner that is there
                if q < row - 1 and grid[q + 1][w] == 1:  # check below
                    perimeter -= 1
                if w > 0 and grid[q][w - 1] == 1:  # check left
                    perimeter -= 1
                if w < col - 1 and grid[q][w + 1] == 1:
                    perimeter -= 1

    return perimeter
