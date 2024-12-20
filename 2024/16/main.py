import time
from Graph import *

INPUT = "input.txt"
TEST = "test_input.txt"

def dijktra(graph):
    dist = {}
    prev = {}
    for n in graph.nodes:
        dist[n] = float("inf")
        prev[n] = [Edge(None, graph.start, ">")]
    q = graph.nodes.copy()
    dist[graph.start] = 0
    
    while q:
        # print(f"remaining: {len(q)}                     ", end = "\r")
        u = min(q, key = lambda x : dist[x])
        q.remove(u)
        
        for edge in u.edges:
            v = edge.dest
            need_to_turn = (prev[u] and any(e.relation != edge.relation for e in prev[u])) and False
            alt = dist[u] + 1 + (1000 if need_to_turn else 0)
            if u.value == "w":
                print(f"u: {u} v: {v} alt: {alt} dist[v]: {dist[v]}")
            if alt <= dist[v]:
                # if need_to_turn:
                #     for e in prev[u]:
                #         e.relation = edge.relation
                if alt < dist[v]:
                    prev[v] = [edge]
                else :
                    prev[v].append(edge)
                dist[v] = alt
                
    return dist, prev
    
def shortest_path(graph, prev):
    path = []
    u = prev[graph.end][0]
    while u and u.src and prev[u.src]:
        path.insert(0, u)
        u = prev[u.src][0]
    return path
    
def print_path(graph, height, width, path):
    if type(path[0]) == list:
        path_as_nodes = []
        for p in path:
            path_as_nodes.extend([node.src for node in p])
    else :
        path_as_nodes = [node.src for node in path]
    for y in range(height):
        for x in range(width):
            if graph.nodes[y*width + x] in path_as_nodes:
                print("O", end = "")
            else:
                print(graph.nodes[y*width+x].value, end = "")
        print()

def print_dist(graph, height, width, dist):
    for y in range(height):
        for x in range(width):
            if graph.nodes[y*width+x].value == "#" :
                print(" #### ", end = "")
            else:
                print(f"{dist[graph.nodes[y*width+x]]:6}", end = "")
        print()

def print_relation(graph, height, width, prev):
    for y in range(height):
        for x in range(width):
            if graph.nodes[y*width+x].value == "#" :
                print("#", end = "")
            elif len(prev[graph.nodes[y*width+x]]) >= 1:
                print(f"{prev[graph.nodes[y*width+x]][0].relation}", end = "")
            else:
                print(" ", end = "")
        print()

def print_prev(graph, height, width, prev):
    for y in range(height):
        for x in range(width):
            if graph.nodes[y*width+x].value == "#" :
                print("#", end = "")
            elif len(prev[graph.nodes[y*width+x]]) >= 1:
                print(f"{len(prev[graph.nodes[y*width+x]])}", end = "")
            else:
                print(" ", end = "")
        print()

def find_all_shortest_paths(graph, prev):
    paths = []
    path_to_add = []
    for edge in prev[graph.end]:
        path_to_add.append([edge])
    while path_to_add:
        print(f"remaining: {len(path_to_add)} and {len(paths)} done                    ", end = "\r")
        path = path_to_add.pop(0)
        u = path[0]
        
        while u and u.src and prev[u.src] and u.src != graph.start:
            if len(prev[u.src]) > 1:
                for edge in prev[u.src][1:]:
                    if edge not in path:
                        new_path = path.copy()
                        new_path.insert(0, edge)
                        path_to_add.append(new_path)
            path.insert(0, u)
            u = prev[u.src][0]
            del prev[u.src][0]
        paths.append(path)
    return paths

def count_seats(path):
    nodes = set()
    for p in path:
        for edge in p:
            nodes.add(edge.src)
            nodes.add(edge.dest)
        
    return len(nodes)

if __name__ == "__main__":
    graph = Graph.from_file("test/4.txt")
    start = time.time()
    dist, prev = dijktra(graph)
    
    wh = 17
    path = shortest_path(graph, prev)
    paths = find_all_shortest_paths(graph, prev)
    print_dist(graph, 14, 52, dist)
    print_relation(graph, 14, 52, prev)
    print_path(graph, 14, 52, paths)
    print_prev(graph, 14, 52, prev)
    
    print(f"\nseats : {count_seats(paths)+1}")
    print(f"just with one path : {len(path)+1}")
    
    print("Time:", time.time() - start)