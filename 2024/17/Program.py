class Instruction():
    def __init__(self, instruction, operand):
        self.instruction = instruction
        self.operand = operand
    
    def __str__(self):
        return f"{self.instruction} {self.operand}"

class Program():
    @classmethod
    def from_file(cls, file_path):
        program = cls()
        with open(file_path, "r") as file:
            line = file.readline().strip()
            program.a = int(line.split("A: ")[1])
            
            line = file.readline().strip()
            program.b = int(line.split("B: ")[1])
            
            line = file.readline().strip()
            program.c = int(line.split("C: ")[1])
            
            file.readline()
            
            line = file.readline().strip()
            line = line.split(" ")[1]
            instructions = line.split(",")
            for i in range(0,len(instructions), 2):
                program.raw_instructions.append(Instruction(int(instructions[i]), int(instructions[i+1])))
            
        return program
    
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.pointer = 0
        self.raw_instructions = []
        self.output = []
        self.print = False
        
        self.combo_match = [
            0,
            1,
            2,
            3,
            "a",
            "b",
            "c",
            None
        ]
        
        self.instructions_match = [
            self.adv,
            self.bxl, # litteral
            self.bst,
            self.jnz, # litteral
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]
    
    def run(self):
        while self.pointer < len(self.raw_instructions):
            instruction = self.raw_instructions[self.pointer]
            if self.run_instruction(instruction):
                return False
            self.pointer += 1
        return ','.join(map(str, self.output))
    
    def print_as_python(self):
        self.print = True
        
        self.run()
        
        self.print = False
    
    def run_instruction(self, instruction : Instruction):
        if instruction.instruction == 1 or instruction.instruction == 3:
            operand = instruction.operand
        else :
            operand = self.combo_match[instruction.operand]
            if not self.print:
                if operand == "a":
                    operand = self.a
                elif operand == "b":
                    operand = self.b
                elif operand == "c":
                    operand = self.c
        return self.instructions_match[instruction.instruction](operand)

    def copy(self):
        new_program = Program()
        new_program.a = self.a
        new_program.b = self.b
        new_program.c = self.c
        new_program.pointer = self.pointer
        new_program.raw_instructions = self.raw_instructions.copy()
        new_program.output = self.output.copy()
        new_program.expected = self.expected.copy()
        return new_program

    def adv(self, combo_op):
        if self.print:
            print(f"a = int(a / pow(2,{combo_op}))")
        else :
            self.a = int(self.a / pow(2,combo_op))

    def bxl(self, literal_op):
        if self.print:
            print(f"b = b ^ {literal_op}")
        else :
            self.b = self.b ^ literal_op

    def bst(self, combo_op):
        if self.print:
            print(f"b = {combo_op} % 8")
        else :
            self.b = combo_op % 8

    def jnz(self, literal_op):
        if self.print:
            print(f"if a == 0 : \n   break; # {literal_op}")
        else :
            if self.a != 0:
                self.pointer = literal_op - 1
            else:
                self.pointer += 1

    def bxc(self, shity_op):
        if self.print:
            print(f"b = b ^ c")
        self.b = self.b ^ self.c

    def out(self, combo_op):
        if self.print:
            print(f"print({combo_op} % 8)")
        else :
            self.output.append(combo_op % 8)

    def bdv(self, combo_op):
        if self.print:
            print(f"b = int(a / pow(2,{combo_op}))")
        else :
            self.b = int(self.a / pow(2, combo_op))

    def cdv(self, combo_op):
        if self.print:
            print(f"c = int(a / pow(2,{combo_op}))")
        else :
            self.c = int(self.a / pow(2, combo_op))