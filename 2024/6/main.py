from time import sleep
import time

def read_input(file_path):
    spaces = []
    with open(file_path, 'r') as file:
        for line in file:
            line = list(line.strip())
            if line:
                spaces.append(line)
    return spaces

def find_positions(spaces):
    directions = ['>', 'v', '<', '^']
    for i in range(len(spaces)):
        for j in range(len(spaces[i])):
            if spaces[i][j] in directions:
                return {"i": i, "j": j}

def move(spaces, positions):
    if positions :
        i = positions['i']
        j = positions['j']
        if spaces[i][j] == '>':
            if (j + 1 >= len(spaces[i])):
                return spaces, None, False
            elif (spaces[i][j + 1] == '.' or spaces[i][j+1] == 'X'):
                spaces[i][j] = 'X'
                spaces[i][j + 1] = '>'
                j = j + 1
            else:
                spaces[i][j] = 'v'
            return spaces, {"i": i, "j": j}, True
        elif spaces[i][j] == 'v':
            if (i + 1 >= len(spaces)):
                return spaces, None, False
            if (spaces[i + 1][j] == '.' or spaces[i + 1][j] == 'X'):
                spaces[i][j] = 'X'
                spaces[i + 1][j] = 'v'
                i = i + 1
            else:
                spaces[i][j] = '<'
            return spaces, {"i": i, "j": j}, True
        elif spaces[i][j] == '<':
            if (j - 1 < 0):
                return spaces, None, False
            if (spaces[i][j - 1] == '.' or spaces[i][j - 1] == 'X'):
                spaces[i][j] = 'X'
                spaces[i][j - 1] = '<'
                j = j - 1
            else:
                spaces[i][j] = '^'
            return spaces, {"i": i, "j": j}, True
        elif spaces[i][j] == '^':
            if (i - 1 < 0):
                return spaces, None, False
            if (spaces[i - 1][j] == '.' or spaces[i - 1][j] == 'X'):
                spaces[i][j] = 'X'
                spaces[i-1][j] = '^'
                i = i - 1
            else:
                spaces[i][j] = '>'
            return spaces, {"i": i, "j": j}, True
        else:
            raise Exception("Invalid direction : " + spaces[i][j])
    else:
        raise Exception("No positions found")


def print_board(spaces):
    for row in spaces:
        print(''.join(row))
    print()

def count_score(spaces):
    score = 0
    for row in spaces:
        for cell in row:
            if cell in ['X', '>', 'v', '<', '^']:
                score += 1
    return score

if __name__ == "__main__":
    input_file = 'input.txt'
    start_time = time.time()
    for i in range(1000):
        spaces = read_input(input_file)
        continue_moving = True
        position = find_positions(spaces)
        while continue_moving:
            spaces, position, continue_moving = move(spaces, position)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(count_score(spaces))
