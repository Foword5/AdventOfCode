TEST_FILE = "test_input.txt"
FILE = "input.txt"

if __name__ == "__main__":
    with open(FILE) as f:
        ranges = []
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            parts = line.split(",")
            for part in parts:
                if part != '' :
                    start, end = map(int, part.split("-"))
                    ranges.append((start, end))
        
        count = 0
        nbr = 0
        for r in ranges:
            nbr += 1
            print(f"Processing range: {nbr}/{len(ranges)}", end="\r")
            for i in range(r[0], r[1] + 1):
                str_i = str(i)
                for y in range(1, len(str_i)//2 +1, 1):
                    if len(str_i)%y != 0:
                        continue
                    parts = [str_i[x:x+y] for x in range(0, len(str_i), y)]
                    if all(p == parts[0] for p in parts):
                        count += i
                        break
        
        print("\ntotal : " + str(count))