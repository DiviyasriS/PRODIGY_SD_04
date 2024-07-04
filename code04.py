def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)

    if empty_cell is None:
        # No empty cell found, puzzle is solved
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            # Try placing the number
            grid[row][col] = num

            # Recursively attempt to solve the rest of the puzzle
            if solve_sudoku(grid):
                return True

            # If placing the number didn't lead to a solution, backtrack
            grid[row][col] = 0

    # No valid number found, need to backtrack
    return False

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def is_valid_move(grid, row, col, num):
    return not used_in_row(grid, row, num) and \
           not used_in_col(grid, col, num) and \
           not used_in_box(grid, row - row % 3, col - col % 3, num)

def used_in_row(grid, row, num):
    for col in range(9):
        if grid[row][col] == num:
            return True
    return False

def used_in_col(grid, col, num):
    for row in range(9):
        if grid[row][col] == num:
            return True
    return False

def used_in_box(grid, box_start_row, box_start_col, num):
    for row in range(3):
        for col in range(3):
            if grid[row + box_start_row][col + box_start_col] == num:
                return True
    return False

def print_sudoku(grid):
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=" ")
        print()

if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku_grid):
        print("Sudoku solved successfully:")
        print_sudoku(sudoku_grid)
    else:
        print("No solution exists for the given Sudoku puzzle.")
