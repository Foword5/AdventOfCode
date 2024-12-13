import re

class Button():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.price = 0
    
    def set_price(self, price):
        self.price = price
        return self

    def __str__(self):
        return f'({self.x}, {self.y})'
    
class Machine():
    @classmethod
    def from_string(cls, lines):
        buttonA_x, buttonA_y = re.findall(r'Button A: X\+([0-9]+), Y\+([0-9]+)', lines[0])[0]
        buttonB_x, buttonB_y = re.findall(r'Button B: X\+([0-9]+), Y\+([0-9]+)', lines[1])[0]
        buttonA = Button(int(buttonA_x), int(buttonA_y))
        buttonB = Button(int(buttonB_x), int(buttonB_y))
        x, y = re.findall(r'Prize: X=([0-9]+), Y=([0-9]+)', lines[2])[0]
        
        return cls(buttonA, buttonB, int(x), int(y))
    
    def __init__(self, buttonA : Button, buttonB : Button, x : int, y : int):
        self.buttonA = buttonA.set_price(3)
        self.buttonB = buttonB.set_price(1)
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Button A : {self.buttonA}\nButton B : {self.buttonB}\nPrize : ({self.x}, {self.y})"
    
    def smallest_path(self):
        for i in range(self.x//self.buttonA.x + 1):
            for j in range(self.x//self.buttonB.x + 1):
                if ((i * self.buttonA.x + j * self.buttonB.x) == self.x and
                    (i * self.buttonA.y + j * self.buttonB.y) == self.y):
                    return {'A': i, 'B': j}
        return None
    
    def smallest_price(self):
        path = self.smallest_path_corrected()
        if path is None:
            return 0
        return path['A'] * self.buttonA.price + path['B'] * self.buttonB.price
    
    def fix_coords(self):
        self.x += 10000000000000
        self.y += 10000000000000
                  
        
    def smallest_path_corrected(self):
        
        for i in range(self.x//self.buttonA.x + 1):
            for j in range(self.x//self.buttonB.x + 1):
                if ((i * self.buttonA.x + j * self.buttonB.x) == self.x and
                    (i * self.buttonA.y + j * self.buttonB.y) == self.y):
                    return {'A': i, 'B': j}
        return None