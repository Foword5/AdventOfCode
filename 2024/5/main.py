INPUT = "input.txt"
TEST = "test_input.txt"

def parse_file(file_name):
    rules_before = {}
    rules_after = {}
    prints = []
    with open(file_name, 'r') as file:
        content = file.read()
        rules_raw, prints_raw = content.split("\n\n")
        
        prints_raw_splited = prints_raw.strip().split("\n")
        for print_line in prints_raw_splited:
            prints.append(print_line.split(","))
        
        for rule in rules_raw.strip().split("\n"):
            before, after = rule.split("|")
            if before not in rules_before:
                rules_before[before] = [after]
            else:
                rules_before[before].append(after)
            if after not in rules_after:
                rules_after[after] = [before]
            else:
                rules_after[after].append(before)
        
    return rules_before, rules_after, prints

def is_print_valid(print_line, rules_before, rules_after):
    total_length = len(print_line)
    
    for i in range(total_length//2 +1):
        if print_line[i] in rules_before:
            for y in range(i):
                if print_line[y] in rules_before[print_line[i]]:
                    return False
    
    for i in range(total_length//2, total_length):
        if print_line[i] in rules_after:
            for y in range(i, total_length):
                if print_line[y] in rules_after[print_line[i]]:
                    return False
    return True

def get_invalid_positions(print_line, rules_before, rules_after):
    total_length = len(print_line)
    
    for i in range(total_length//2 +1):
        if print_line[i] in rules_before:
            for y in range(i):
                if print_line[y] in rules_before[print_line[i]]:
                    return i,y
    
    for i in range(total_length//2, total_length):
        if print_line[i] in rules_after:
            for y in range(i, total_length):
                if print_line[y] in rules_after[print_line[i]]:
                    return i,y
    return 0,0
    
def correct_print(print_line, rules_before, rules_after):
    i, j = get_invalid_positions(print_line, rules_before, rules_after)
    while (i,j) != (0,0):
        
        temp = print_line[i]
        print_line[i] = print_line[j]
        print_line[j] = temp
        
        i, j = get_invalid_positions(print_line, rules_before, rules_after)
    
    return print_line
    
if __name__ == "__main__":
    rules_before, rules_after, prints = parse_file(INPUT)
    
    total = 0
    for print_line in prints:
        if not is_print_valid(print_line, rules_before, rules_after):
            corrected_print_line = correct_print(print_line, rules_before, rules_after)
            total += int(corrected_print_line[len(corrected_print_line) // 2])
    print("Q1",total)
    
    total = 0
    for print_line in prints:
        if is_print_valid(print_line, rules_before, rules_after):
            total += int(print_line[len(print_line) // 2])
    
    print("Q2", total)
