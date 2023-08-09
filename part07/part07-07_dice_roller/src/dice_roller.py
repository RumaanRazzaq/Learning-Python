# Write your solution here
from random import shuffle, sample

def roll(die: str):
    die_a = [3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]
    
    if die == "A":
        return sample(die_a, 1)[0]
    elif die == "B":
        return sample(die_b, 1)[0]
    elif die == "C":
        return sample(die_c, 1)[0]
    
def play(die1: str, die2: str, times: int):
    die_a = [3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]

    p1_wins = 0
    p2_wins = 0
    ties = 0

    for i in range(0, times):
        p1_turn = 0
        p2_turn = 0

        if die1 == "A":
            p1_turn = sample(die_a, 1)[0]
        elif die1 == "B":
            p1_turn = sample(die_b, 1)[0]
        elif die1 == "C":
            p1_turn = sample(die_c, 1)[0]
    
        if die2 == "A":
            p2_turn = sample(die_a, 1)[0]
        elif die2 == "B":
            p2_turn = sample(die_b, 1)[0]
        elif die2 == "C":
            p2_turn = sample(die_c, 1)[0]

        if p1_turn > p2_turn:
            p1_wins += 1
        elif p2_turn > p1_turn:
            p2_wins += 1
        else:
            ties += 1
    
    return(p1_wins, p2_wins, ties)

if __name__ == "__main__":

    for i in range(20):
        print(roll("A"), " ", end="")
    print()

    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    
    for i in range(20):
        print(roll("C"), " ", end="")
    print()

    print()
    
    result = play("A", "C", 1000)
    print(result)

    result = play("B", "B", 1000)
    print(result)