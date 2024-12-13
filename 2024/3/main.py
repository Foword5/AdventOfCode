import re

def find_mul(string):
    return re.findall(r'mul\(([0-9]{1,3}?),([0-9]{1,3}?)\)', string)

def multiply_all(string):
    mul = find_mul(string)
    sum = 0
    for i in mul:
        sum += int(i[0]) * int(i[1])
    return sum

def multiply_all_with_do(string):
    sum = 0
    do = True
    for i in range(len(string)):
        if string[i:i+4] == 'mul(' and do:
            mul = find_mul(string[i:i+12])
            if mul:
                sum += int(mul[0][0]) * int(mul[0][1])
        if string[i:i+4] == 'do()':
            do = True
        if string[i:i+7] == "don't()":
            do = False
    return sum

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()

    print(multiply_all_with_do(data))