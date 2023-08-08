# Write your solution here
def column_correct(sudoku: list, column_no: int):
    new_list = []
    for i in range(0, 9):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] in new_list:
            return False
        else:
            new_list.append(sudoku[i][column_no])
    return True