# Write your solution here
def who_won(game_board: list):
    ones = 0
    twos = 0
    for row in game_board:
        for element in row:
            if element == 1:
                ones += 1
            elif element == 2:
                twos += 1
    if ones > twos:
        return 1
    elif twos > ones:
        return 2
    else: 
        return 0