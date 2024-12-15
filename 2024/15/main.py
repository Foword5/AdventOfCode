from Room import Room

INPUT = "input.txt"
TEST = "test_input.txt"
SMALL = "small_test_input.txt"

if __name__ == "__main__":
    room = Room.create_big_from_file(INPUT)
    print(room)
    room.follow_instructions(True)
    print(room)
    print(room.get_GPS(big=True))