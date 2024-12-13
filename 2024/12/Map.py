class Space():
    def __init__(self, color):
        self.color = color
        self.neighbors = {
            "up": None,
            "down": None,
            "left": None,
            "right": None
        }
        self.visited = False
        self.border = None

    def add_neighbor(self, direction, neighbor):
        self.neighbors[direction] = neighbor
    
    def visit(self):
        self.visited = True
    
    def get_border(self):
        if self.border is None:
            self.border = 4 - len(self.same_color_neighbor())
        return self.border
    
    def same_color_neighbor(self):
        neighbors = []
        for neighbor in self.neighbors.values():
            if neighbor != None and neighbor.color == self.color:
                neighbors.append(neighbor)
        self.border = 4 - len(neighbors)
        return neighbors
        

    def __str__(self):
        return f"{self.color}, neighbors: {self.neighbors}"

class Map():
    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            lines = f.readlines()
            new_map = cls(len(lines[0])-1, len(lines))
            
            for y, line in enumerate(lines):
                for x, color in enumerate(line):
                    if color != "\n":
                        new_map.add_space(x, y, color)
            return new_map
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaces = [[None for _ in range(width)] for _ in range(height)]
        self.zones = []
    
    def add_space(self, x, y, color):
        self.spaces[y][x] = Space(color)
    
    def fill_neighbors(self):
        for y, line in enumerate(self.spaces):
            for x, space in enumerate(line):
                if space is not None:
                    if y > 0:
                        space.add_neighbor("up", self.spaces[y-1][x])
                    if y < self.height - 1:
                        space.add_neighbor("down", self.spaces[y+1][x])
                    if x > 0:
                        space.add_neighbor("left", self.spaces[y][x-1])
                    if x < self.width - 1:
                        space.add_neighbor("right", self.spaces[y][x+1])
    
    def unvisit_all(self):
        for line in self.spaces:
            for space in line:
                if space is not None:
                    space.visited = False
    
    def define_zones(self):
        self.zones = []
        self.unvisit_all()
        for y, line in enumerate(self.spaces):
            for x, space in enumerate(line):
                if space is not None and not space.visited:
                    zone = create_zone_rec(space, [])
                    self.zones.append(zone)

    def get_cost(self):
        cost = 0
        for zone in self.zones:
            border = 0
            for space in zone:
                border += space.get_border()
            cost += border * len(zone)
        return cost
    
    def __str__(self):
        string = ""
        for line in self.spaces :
            for space in line:
                string += str(space.color)
            string += "\n"
        return string
    
def create_zone_rec(space : Space, zone : list):
    zone.append(space)
    space.visit()
    for neighbor in space.same_color_neighbor():
        if not neighbor.visited :
            zone = create_zone_rec(neighbor, zone)
    return zone