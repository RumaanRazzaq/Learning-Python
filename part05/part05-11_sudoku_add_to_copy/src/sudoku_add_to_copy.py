# Write your solution here
def print_sudoku(sudoku: list):
    i = 0
    j = 0
    space =  True
    for row in sudoku:
        for item in row:
            if j == 3:
                if space == False:
                    space = True
                else:
                    print(" ", end = "")
                j = 0
            if item == 0:
                print("_ ", end="")
                j += 1
            else:
                print(f"{item} ", end="")
                j += 1
        print()
        i += 1
        space = False
        if i == 3:
            print()
            i = 0
            
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_grid = []
    for row in sudoku:
        new_grid.append(row[:])    
    new_grid[row_no][column_no] = number
    return new_grid

if __name__ == "__main__":
    
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)