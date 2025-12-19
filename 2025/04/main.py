TEST_FILE = "test_input.txt"
FILE = "input.txt"

def too_many_adjacent(rolls, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(rolls) and 0 <= c < len(rolls[0]):
            if rolls[r][c] == '@':
                count += 1
                if count >= 4:
                    return True
    return False

if __name__ == "__main__":
    rolls = []
    with open(FILE) as f:
        lines = f.readlines()
        for line in lines:
            rolls.append(list(line.strip()))

    total_removed = 0
    
    removed_one = True
    while removed_one:
        removed_one = False
        for r in range(len(rolls)):
            for c in range(len(rolls[0])):
                if rolls[r][c] == '@':
                    if not too_many_adjacent(rolls, r, c):
                        total_removed += 1
                        rolls[r][c] = '.'
                        removed_one = True

    print("Total adjacent '@' characters:", total_removed)

