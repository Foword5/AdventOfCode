INPUT = "input.txt"
TEST = "test_input.txt"

def file_to_list(file):
    with open(file) as f:
        return [list(line.strip()) for line in f]

def get_with_catch(x, y, list):
    if x < 0 or y < 0:
        return None
    try:
        return list[x][y]
    except:
        return None

def is_start_of_xmas(x, y, xmas):
    direction  = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    count = 0
    
    for d in direction:
        pos_x = x
        pos_y = y
        string = "X"
        for i in ["M","A","S"]:
            pos_x += d[0]
            pos_y += d[1]
            string += str(get_with_catch(pos_x, pos_y, xmas))
        if string == "XMAS":
            count += 1
    return count

def find_xmas(xmas):
    count = 0
    for x in range(len(xmas)):
        for y in range(len(xmas[x])):
            if xmas[x][y] == "X":
                count += is_start_of_xmas(x, y, xmas)
    return count

def is_center_of_x_shape_mas(x, y, xmas):
    left_up = get_with_catch(x-1, y-1, xmas)
    right_up = get_with_catch(x-1, y+1, xmas)
    left_down = get_with_catch(x+1, y-1, xmas)
    right_down = get_with_catch(x+1, y+1, xmas)
    l = [left_up, left_down, right_down, right_up]
    
    return l.count("M") == 2 and l.count("S") == 2 and left_up != right_down and left_down != right_up

def count_x_shape_mas(xmas):
    count = 0
    for x in range(len(xmas)):
        for y in range(len(xmas[x])):
            if xmas[x][y] == "A":
                count += is_center_of_x_shape_mas(x, y, xmas)
    return count

if __name__ == "__main__":
    xmas = file_to_list(INPUT)
    print(count_x_shape_mas(xmas))