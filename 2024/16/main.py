from Board import *

INPUT = "input.txt"
TEST = "test_input.txt"

def dijkstra(board):
    q = []
    for row in board.board:
        for vertex in row:
            q.append(vertex)

    while q:
        print(f"element in q: {len(q)}", end="\r")
        q.sort(key=lambda x: x.dist)
        u = q[0]
        q.remove(u)
        
        for direction,n in u.neighbors.items():
            if n == None or n not in q :
                continue
            alt = u.dist + calc_distance(u, direction)
            if alt < n.dist :
                n.direction = direction
                n.dist = alt
                n.prev = u
                
def calc_distance(source, neighbor_direction):
    if source.direction == None :
        raise ValueError("Source vertex has no direction")
    if source.direction == neighbor_direction :
        return 1
    else :
        return 1001
        
def shortest_path(board):
    dijkstra(board)
    path = []
    u = board.board[board.end[1]][board.end[0]]
    while u.prev:
        path.insert(0, u)
        u = u.prev
    path.insert(0, u)
    return path

def print_path(path):
    for vertex in path:
        vertex.char = vertex.direction

def calc_path_price(path):
    price = 0
    last = path[0]
    for vertex in path[1:]:
        price += calc_distance(last, vertex.direction)
        last = vertex
        
    return price

if __name__ == "__main__":
    board = Board.from_file(INPUT)
    path = shortest_path(board)
    print_path(path)
    print(board)
    print(calc_path_price(path))
    
