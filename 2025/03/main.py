TEST_FILE = "test_input.txt"
FILE = "input.txt"

def maxWithIndex(list, start, end) : 
    max = -1
    index = -1
    for i in range(start, end): 
        if list[i] > max: 
            max = list[i]
            index = i
    return max, index

if __name__ == "__main__":
    banks = []
    with open(FILE) as f:
        lines = f.readlines()
        for line in lines:
            banks.append([int(x) for x in list(line.strip())])

    voltage = 0
    for bank in banks:
        value = ""
        partial_bank = bank.copy()
        index = 0
        for i in range(11, -1, -1):
            temp_value, index = maxWithIndex(bank, index, len(bank) - i)
            index += 1
            value += str(temp_value)
        voltage += int(value)

    print("Total voltage:", voltage)
        

