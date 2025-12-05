TEST_FILE = "test_input.txt"
FILE = "input.txt"

if __name__ == "__main__":
    with open(FILE) as f:
        lines = f.readlines()
        nbr = 50
        count = 0
        for line in lines:
            line = line.strip()
            direction = line[0]
            clics = int(line[1:])
            while clics > 0:
                if direction == "L":
                    nbr -= 1
                elif direction == "R":
                    nbr += 1
                clics -= 1
                nbr = nbr % 100
                if nbr == 0:
                    count += 1

        print(count)