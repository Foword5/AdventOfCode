from randomShit import count_stone_after_blink
import time

seen = {}

def blinkRec(object, blinks):
    if object in seen:
        return seen[object]
    if blinks == 0:
        return 1
    
    if object == 0:
        value = blinkRec(1, blinks-1)
        seen[object] = value
        return value
    
    castedElement = str(object)
    length = len(castedElement)
    if length % 2 == 0:
        value = blinkRec(int(castedElement[length//2:]), blinks-1) + blinkRec(int(castedElement[:length//2]), blinks-1)
    else:
        value = blinkRec(object * 2024, blinks-1)
    seen[object] = value
    return value

def blink(list, blinks):
    nbr = 0
    for object in list:
        nbr += blinkRec(object, blinks)
    return nbr

def blinkRecWithReturn(object, blinks) -> list:
    print(object, blinks)
    if blinks == 0:
        return [object]
    
    value = -1

    if object == 0:
        value = blinkRecWithReturn(1, blinks-1)
    
    castedElement = str(object)
    length = len(castedElement)
    if length % 2 == 0:
        value = blinkRecWithReturn(int(castedElement[length//2:]), blinks-1).extend(blinkRecWithReturn(int(castedElement[:length//2]), blinks-1))
    else:
        value = blinkRecWithReturn(object * 2024, blinks-1)

    return value

def blinkWithReturn(list, blinks):
    nbr = []
    for object in list:
        nbr.extend(blinkRecWithReturn(object, blinks))
    return nbr

if __name__ == "__main__":
    list = [965842, 9159, 3372473, 311, 0, 6, 86213, 48]
    
    blinks = 3

    # start_time = time.time()
    # print(count_stone_after_blink(list, blinks))
    # print(f"took {time.time() - start_time}s")

    list = [125, 17]

    start_time = time.time()
    print(blinkWithReturn(list, blinks))
    print(f"took {time.time() - start_time}s")