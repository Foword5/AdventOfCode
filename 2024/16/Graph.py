class Graph :
    @classmethod
    def from_file(cls, file) :
        with open(file, 'r') as f :
            lines = f.readlines()
            
            newGraph = cls()
            
            nodes = []
            for line in lines :
                newLine = []
                for char in line.strip() :
                    newLine.append(Node(char))
                    if char == "S" :
                        newGraph.start = newLine[-1]
                    if char == "E" :
                        newGraph.end = newLine[-1]
                    newGraph.nodes.append(newLine[-1])
                nodes.append(newLine)
            
            for y, line in enumerate(nodes) :
                for x, node in enumerate(line) :
                    if y > 0 and nodes[y-1][x].value != "#" :
                        edge = Edge(node, nodes[y-1][x], "^")
                        newGraph.edges.append(edge)
                        node.edges.append(edge)
                    if y < len(nodes) - 1 and nodes[y+1][x].value != "#" :
                        edge = Edge(node, nodes[y+1][x], "v")
                        newGraph.edges.append(edge)
                        node.edges.append(edge)
                    if x > 0 and nodes[y][x-1].value != "#" :
                        edge = Edge(node, nodes[y][x-1], "<")
                        newGraph.edges.append(edge)
                        node.edges.append(edge)
                    if x < len(line) - 1 and nodes[y][x+1].value != "#" :
                        edge = Edge(node, nodes[y][x+1], ">")
                        newGraph.edges.append(edge)
                        node.edges.append(edge)
                
        return newGraph
    
    def __init__(self) :
        self.nodes = []
        self.edges = []
        self.start = None
        self.edn = None

    def print(self, height, width) :
        for y in range(height) :
            for x in range(width) :
                print(self.nodes[y*width+x].value, end = "")
            print()

class Node :
    def __init__(self, value) :
        self.value = value
        self.edges = []
    
    def __str__(self) :
        return self.value

class Edge :
    def __init__(self, src, dest, relation, weight = 1) :
        self.src = src
        self.dest = dest
        self.weight = weight
        self.relation = relation
    
    def __str__(self) :
        return f'{self.src.value} {self.relation} {self.dest.value}'