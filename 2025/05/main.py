TEST_FILE = "test_input.txt"
FILE = "input.txt"

if __name__ == "__main__":

    fresh_ranges = []
    ids = []

    with open(FILE) as f:
        lines = f.readlines()
        
        line = lines.pop(0).strip()
        while line != '':
            parts = line.split('-')
            fresh_ranges.append((int(parts[0]), int(parts[1])))
            line = lines.pop(0).strip()
        
    fresh_ranges.sort()
    
    new_ranges = []

    nbr = 0
    for r in fresh_ranges:
        nbr += 1
        print(f"Processing range: {nbr}/{len(fresh_ranges)}", end='\r')
        updated = False
        for nr in new_ranges:
            if nr[0] <= r[0] <= nr[1] or nr[0] <= r[1] <= nr[1]:
                nr[0] = min(nr[0], r[0])
                nr[1] = max(nr[1], r[1])
                updated = True
                break
            
        if not updated:
            new_ranges.append([r[0], r[1]])

    total = 0
    for r in new_ranges:
        total += r[1] - r[0] + 1

    print("\n total = " + str(total))