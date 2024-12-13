from Map import *

if __name__ == '__main__':
    map = Map.from_file("input.txt")
    map.fill_neighbors()
    map.define_zones()
    print(map.get_discounted_cost())