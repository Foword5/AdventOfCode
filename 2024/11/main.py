from randomShit import count_stone_after_blink
import time

seen = {}

def blinkRec(object, blinks):
    if object in seen:
        if blinks in seen[object]:
            return seen[object][blinks]
    else:
        seen[object] = {}
        
    if blinks == 0:
        return 1
    
    if object == 0:
        value = blinkRec(1, blinks-1)
        seen[object][blinks] = value
        return value
    
    castedElement = str(object)
    length = len(castedElement)
    if length % 2 == 0:
        value = blinkRec(int(castedElement[length//2:]), blinks-1) + blinkRec(int(castedElement[:length//2]), blinks-1)
        seen[object][blinks] = value
        return value
    
    value = blinkRec(object * 2024, blinks-1)
    seen[object][blinks] = value
    return value

def blink(list, blinks):
    nbr = 0
    for object in list:
        nbr += blinkRec(object, blinks)
    return nbr

if __name__ == "__main__":
    list = [965842, 9159, 3372473, 311, 0, 6, 86213, 48]
    
    blinks = 75

    start_time = time.time()
    print(blink(list, blinks))
    print(f"took {time.time() - start_time}s")