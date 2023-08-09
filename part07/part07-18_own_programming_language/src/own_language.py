# Write your solution here
from string import ascii_uppercase

def run(program):
    print_list = []
    
    variable = {}

    for char in ascii_uppercase:
        variable[char] = 0
    
    for i in range(len(program)):
        #print(i)
        #print()
        command_words = program[i].split(" ")
        if command_words[0] == "END":
            break
        elif command_words[0] == "MOV":
            pass
            #variable[command_words[1]] = int(command_words[2])
        elif command_words[0] == "ADD":
            variable[command_words[1]] += variable[command_words[2]]
        elif command_words[0] == "PRINT":
            print_list.append(variable[command_words[1]])
        elif command_words[0] == "SUB":
            pass
            #variable[command_words[1]] -= variable[command_words[2]]
        elif command_words[0] == "MUL":
            variable[command_words[1]] *= variable[command_words[2]]
        elif command_words[0] == "JUMP":
            temp = 0
            label = command_words[1]
            for command in program:
                comparison = command.split(":")[0]
                if comparison == label:
                    #print(temp)
                    break
                temp += 1
        elif command_words[0] == "IF":
            pass

    return print_list

if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("JUMP begin")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("begin:")
    program1.append("END")
    result = run(program1)
    program2 = ['MOV A 10', 'PRINT A', 'MOV B A', 'SUB B 8', 'PRINT B', 'SUB A B', 'PRINT A']
    result2 = run(program2)
    print(result)
    print(result2)