# Write your solution here
def row_correct(sudoku: list, row_no: int):
    new_list = []
    for i in range(0, 9):
        if sudoku[row_no][i] > 0 and sudoku[row_no][i] in new_list:
            return False
        else:
            new_list.append(sudoku[row_no][i])
    return True