from Program import *

INPUT = "input.txt"
TEST = "test_input.txt"
TEST2 = "test2.txt"

if __name__ == "__main__":
    program = Program.from_file(INPUT)
    program.print_as_python()