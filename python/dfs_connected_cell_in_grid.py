"""
DFS: Connected Cell in a Grid

https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid

Consider a matrix with n rows and m columns, where each cell contains either a 0 or a 1 and any cell containing a 1 is
called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically,
or diagonally.

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at
least one other cell in the region but is not necessarily directly connected to all the other cells in the region.

Output Format
Given an n * m matrix, find and print the number of cells in the largest region in the matrix. Note that there may be
more than one region in the matrix.

Sample Input
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

Sample Output
5
"""


def traverse(start_row, start_col, grid, visited, linked):
    if (start_row, start_col) in visited:
        return

    if 0 <= start_row < len(grid) and 0 <= start_col < len(grid[0]):
        visited.add((start_row, start_col))

        if grid[start_row][start_col] == 1:
            linked.append((start_row, start_col))

            traverse(start_row - 1, start_col - 1, grid, visited, linked)
            traverse(start_row - 1, start_col, grid, visited, linked)
            traverse(start_row - 1, start_col + 1, grid, visited, linked)
            traverse(start_row, start_col - 1, grid, visited, linked)
            traverse(start_row, start_col + 1, grid, visited, linked)
            traverse(start_row + 1, start_col - 1, grid, visited, linked)
            traverse(start_row + 1, start_col, grid, visited, linked)
            traverse(start_row + 1, start_col + 1, grid, visited, linked)


def get_biggest_region(grid):
    visited = set()
    max_cnt = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            linked = []
            traverse(row, col, grid, visited, linked)
            max_cnt = max(max_cnt, len(linked))
            col += 1
        row += 1
    return max_cnt


if __name__ == '__main__':
    orig_grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    print(get_biggest_region(orig_grid))
