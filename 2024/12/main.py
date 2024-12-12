from Map import *

if __name__ == '__main__':
    map = Map.from_file("input.txt")
    create_zone_rec(map.spaces[0][0], [])
    print(map)