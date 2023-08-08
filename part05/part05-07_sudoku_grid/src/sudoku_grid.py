# Write your solution here
def row_correct(sudoku: list, row_no: int):
    new_list = []
    for i in range(0, 9):
        if sudoku[row_no][i] > 0 and sudoku[row_no][i] in new_list:
            return False
        else:
            new_list.append(sudoku[row_no][i])
    return True

def column_correct(sudoku: list, column_no: int):
    new_list = []
    for i in range(0, 9):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] in new_list:
            return False
        else:
            new_list.append(sudoku[i][column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list = []
    for row in range(row_no, row_no+3):
        for element in range(column_no, column_no+3):
            number = sudoku[row][element]
            if number > 0 and number in new_list:
                return False
            new_list.append(number)
 
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
 
    return True