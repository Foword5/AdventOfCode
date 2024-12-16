from Machine import Machine
import time

INPUT_FILE = 'input.txt'
TEST_FILE = 'test_input.txt'

def solve_doube_unknown_equation(total1, factor1a, factor1b, total2, factor2a, factor2b):
    total3 = total1 * factor2a
    factor3a = factor1a * factor2a
    factor3b = factor1b * factor2a
    # print(f"{total3} = {factor3a}*a + {factor3b}*b")
    
    total4 = total2 * factor1a
    factor4a = factor2a * factor1a
    factor4b = factor2b * factor1a
    # print(f"{total4} = {factor4a}*a + {factor4b}*b")
    
    total34 = total3 - total4
    factor34a = factor3a - factor4a
    factor34b = factor3b - factor4b
    # print(f"{total34} = {factor34a}*a + {factor34b}*b")
    
    b = total34 / factor34b
    # print(f"b = {b}")
    
    a = (total1 - b * factor1b) / factor1a
    # print(f"a = {a}")
    
    return a, b

if __name__ == '__main__':
    machines = []
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            machines.append(Machine.from_string(lines[i:i+3]))
            
    start = time.time()
    
    cost = 0
    for machine in machines:
        machine.fix_coords()
        total1 = machine.x
        factor1a = machine.buttonA.x
        factor1b = machine.buttonB.x
        total2 = machine.y
        factor2a = machine.buttonA.y
        factor2b = machine.buttonB.y
        a, b = solve_doube_unknown_equation(total1, factor1a, factor1b, total2, factor2a, factor2b)
        if not (a.is_integer() and b.is_integer()):
            continue
        a = int(a)
        b = int(b)
        cost += machine.buttonA.price * a + machine.buttonB.price * b
    
    print(cost)
    end = time.time()
