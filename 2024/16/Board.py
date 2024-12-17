class Board():
    @classmethod
    def from_file(cls, file):
        with open(file, 'r') as f:
            lines = f.readlines()
            height, width = len(lines), len(lines[0].strip())
            newBoard = cls(height, width)
            
            for y, line in enumerate(lines):
                newLine = []
                for x, char in enumerate(line.strip()):
                    if char == "S":
                        newBoard.start = (x, y)
                        newLine.append(Vertex(x, y, char, 0, ">"))
                        newBoard.all_vertices.append(newLine[-1])
                        continue
                    if char == "E":
                        newBoard.end = (x, y)
                    newLine.append(Vertex(x, y, char))
                    newBoard.all_vertices.append(newLine[-1])
                newBoard.board.append(newLine)
        
        for y in range(newBoard.height):
            for x in range(newBoard.width):
                newBoard.set_neighbors(x, y)
        
        return newBoard
    
    def set_neighbors(self, x, y):
        if y > 0:
            neighbor = self.board[y-1][x]
            if neighbor.char != "#":
                self.board[y][x].neighbors["^"] = neighbor
        if y < self.height - 1:
            neighbor = self.board[y+1][x]
            if neighbor.char != "#":
                self.board[y][x].neighbors["v"] = neighbor
        if x > 0:
            neighbor = self.board[y][x-1]
            if neighbor.char != "#":
                self.board[y][x].neighbors["<"] = neighbor
        if x < self.width - 1:
            neighbor = self.board[y][x+1]
            if neighbor.char != "#":
                self.board[y][x].neighbors[">"] = neighbor

    def __init__(self, height, width):
        self.all_vertices = []
        self.height = height
        self.width = width
        self.board = []
        self.start = None
        self.end = None

    def __str__(self):
        string = f'Height: {self.height}\nWidth: {self.width}\nStart: {self.start}\nEnd: {self.end}\n'
        string += "\n".join(["".join([space.char for space in line]) for line in self.board])
        return string

    def copy(self):
        newBoard = Board(self.height, self.width)
        newBoard.all_vertices = [vertex for vertex in self.all_vertices]
        newBoard.board = [line for line in self.board]
        newBoard.start = self.start
        newBoard.end = self.end
        newBoard.height = self.height
        newBoard.width = self.width
        return newBoard

class Vertex():
    def __init__(self, x, y, char, dist = float("inf"), direction = None):
        self.x = x
        self.y = y
        self.char = char
        self.dist = dist
        self.direction = direction
        self.prev = None
        self.neighbors = {
            "^": None,
            "v": None,
            "<": None,
            ">": None
        }
    
    def __str__(self):
        return f"({self.x}, {self.y}) {self.char} : {self.dist} away, going {self.direction}, pred : {self.prev.x if self.prev else None}, {self.prev.y if self.prev else None}"
