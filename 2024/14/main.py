from Room import Room

INPUT = "input.txt"
TEST = "test_input.txt"

if __name__ == "__main__":
    real_room = Room.create_from_file(101, 103, INPUT)
    test_room = Room.create_from_file(11, 7, TEST)
    
    
    iter = 0
    while not real_room.look_for_chrismas_tree() and iter < 100000:
        iter += 1
        print(iter, end='\r')
        real_room.second_pass()
    
    real_room.visualise()
    
    print(iter)
    