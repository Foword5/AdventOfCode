class Room():
    @classmethod
    def create_from_file(cls, filename):
        with open(filename, 'r') as f:
            line = f.readline()
            height = 0
            width = len(line.strip())
            while line.strip() != "":
                height += 1
                line = f.readline()
            room = cls(width, height)
            
            f.seek(0)
            
            line = f.readline()
            y = 0
            while line.strip() != "":
                for x in range(width):
                    room.set_tile(x, y, line[x])
                    if line[x] == '@':
                        room.bot_x = x
                        room.bot_y = y
                y += 1
                line = f.readline()
            
            while line := f.readline():
                for instruction in line.strip():
                    room.add_instruction(instruction)
            
        return room

    @classmethod
    def create_big_from_file(cls, filename):
        with open(filename, 'r') as f:
            line = f.readline()
            height = 0
            width = len(line.strip())
            while line.strip() != "":
                height += 1
                line = f.readline()
            room = cls(width*2, height)
            
            f.seek(0)
            
            line = f.readline()
            y = 0
            while line.strip() != "":
                for x in range(width):
                    room.set_tile(x*2, y, line[x])
                    if line[x] == 'O':
                        room.set_tile(x*2, y, "[")
                        room.set_tile(x*2+1, y, "]")
                    elif line[x] == '@':
                        room.bot_x = x*2
                        room.bot_y = y
                        room.set_tile(x*2+1, y, ".")
                    else:
                        room.set_tile(x*2+1, y, line[x])
                y += 1
                line = f.readline()
            
            while line := f.readline():
                for instruction in line.strip():
                    room.add_instruction(instruction)
            
        return room
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bot_x = None
        self.bot_y = None
        self.tiles = [[' ' for x in range(width)] for y in range(height)]
        self.instructions = []
        
    def set_tile(self, x, y, tile):
        if x < 0 or x >= self.width:
            raise ValueError("x is out of bounds")
        self.tiles[y][x] = tile
    
    def get_tile(self, x, y):
        if x < 0 or x >= self.width:
            raise ValueError("x is out of bounds")
        return self.tiles[y][x]

    def add_instruction(self, instruction):
        self.instructions.append(instruction)
        
    def move_bot(self, direction):
        nbr_direction = {"x": None, "y": None}
        if direction == ">":
            nbr_direction["x"] = 1
            nbr_direction["y"] = 0
        elif direction == "<":
            nbr_direction["x"] = -1
            nbr_direction["y"] = 0
        elif direction == "^":
            nbr_direction["x"] = 0
            nbr_direction["y"] = -1
        elif direction == "v":
            nbr_direction["x"] = 0
            nbr_direction["y"] = 1
        else:
            raise ValueError("Invalid direction")
        
        if self._move_rec(self.bot_x, self.bot_y, nbr_direction):
            self.set_tile(self.bot_x, self.bot_y, '.')
            self.bot_x += nbr_direction["x"]
            self.bot_y += nbr_direction["y"]
    
    def _move_rec(self, x, y, direction):
        tile = self.get_tile(x, y)
        if tile == '#':
            return False
        if tile == '.':
            return True
        if self._move_rec(x + direction["x"], y+direction["y"], direction):
            self.set_tile(x + direction["x"], y+direction["y"], tile)
            return True
        return False
    
    def follow_instructions(self, big=False):
        for instruction in self.instructions:
            if big:
                self.move_bot_big(instruction)
            else:
                self.move_bot(instruction)
            
    def move_bot_big(self, direction):
        nbr_direction = {"x": None, "y": None}
        if direction == ">":
            nbr_direction["x"] = 1
            nbr_direction["y"] = 0
        elif direction == "<":
            nbr_direction["x"] = -1
            nbr_direction["y"] = 0
        elif direction == "^":
            nbr_direction["x"] = 0
            nbr_direction["y"] = -1
        elif direction == "v":
            nbr_direction["x"] = 0
            nbr_direction["y"] = 1
        else:
            raise ValueError("Invalid direction")
        
        if self._can_move_rec_big(self.bot_x, self.bot_y, nbr_direction):
            self._move_rec_big(self.bot_x, self.bot_y, nbr_direction)
    
    def _can_move_rec_big(self, x, y, direction, send_from_half=False):
        tile = self.get_tile(x, y)
        if tile == '#' or not tile:
            return False
        if tile == '.':
            return True
        if tile == '[' and not send_from_half:
            if direction["x"] == 1:
                return self._can_move_rec_big(x+1, y, direction, True)
            return (self._can_move_rec_big(x + direction["x"], y+direction["y"], direction) and 
                    self._can_move_rec_big(x+1, y, direction, True))
        if tile == ']' and not send_from_half:
            if direction["x"] == -1:
                return self._can_move_rec_big(x-1, y, direction, True)
            return (self._can_move_rec_big(x + direction["x"], y+direction["y"], direction) and 
                    self._can_move_rec_big(x-1, y, direction, True))
            
        return self._can_move_rec_big(x + direction["x"], y + direction["y"], direction)
    
    def _move_rec_big(self, x, y, direction, send_from_half=False):
        tile = self.get_tile(x, y)
        if tile == '#' or not tile or tile == '.':
            return 
        self.set_tile(x, y, '.')
        
        if tile == '[' and not send_from_half and direction["x"] != 1:
                self._move_rec_big(x+1, y, direction, True)
        elif tile == ']' and not send_from_half and direction["x"] != -1:
                self._move_rec_big(x-1, y, direction, True)
                
        self._move_rec_big(x + direction["x"], y+direction["y"], direction)
        self.set_tile(x + direction["x"], y+direction["y"], tile)
        if tile == '@':
            self.bot_x += direction["x"]
            self.bot_y += direction["y"]
        return True
            
    def get_GPS(self, big=False):
        count = 0
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if (not big and tile != 'O') or (big and tile != '['):
                    continue
                count += 100 * y + x
        return count
    
    def __str__(self):
        return "\n".join(["".join(row) for row in self.tiles]) + "\n" + ",".join(self.instructions) + "\n" + f"Bot: {self.bot_x}, {self.bot_y}"