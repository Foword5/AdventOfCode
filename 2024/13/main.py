from Machine import Machine
import time

INPUT_FILE = 'input.txt'
TEST_FILE = 'test_input.txt'

if __name__ == '__main__':
    machines = []
    with open(TEST_FILE, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            machines.append(Machine.from_string(lines[i:i+3]))
            
    start = time.time()
    
    x = 10000000008400
    # x = 8400
    ax = 94
    bx = 22
    
    y = 10000000005400
    # y = 5400
    ay = 34
    by = 67
    
    # nba = 10000000008400//ax + 2
    # nbb = 0
    
    # while nba*ax + nbb*bx != x:
    #     nba -= 1
    #     while nba*ax + nbb*bx < x:
    #         nbb += 1

    nba = x//ax + 2
    nbb = 0

    while nba*ay + nbb*by != y or nba*ax + nbb*bx != x:
        print(nba*ay + nbb*by, nba*ax + nbb*bx)
        if nba*ay + nbb*by < y:
            nbb += abs(y - (nba*ay + nbb*by)) // by
            nba -= abs(y - (nba*ay + nbb*by)) // ay
        elif nba*ay + nbb*by > y:
            nbb -= abs(y - (nba*ay + nbb*by)) // by
            nba += abs(y - (nba*ay + nbb*by)) // ay
            
        if nba*ax + nbb*bx < x:
            nbb -= abs(x - (nba*ax + nbb*bx)) // bx
            nba += abs(x - (nba*ax + nbb*bx)) // ax
        elif nba*ax + nbb*bx > x:
            nba -= abs(x - (nba*ax + nbb*bx)) // ax
            nbb += abs(x - (nba*ax + nbb*bx)) // bx
    
    print(nba*ax + nbb*bx, nba*ay + nbb*by)
        
    end = time.time()
    