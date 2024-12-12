def blinkNode(element : int) -> list:
    castedElement = str(element)
    length = len(castedElement)
    if element == 0:
        return [1]
    elif length % 2 == 0:
        value1, value2 = int(castedElement[length//2:]) , int(castedElement[:length//2])
        return [value1, value2]
    else:
        return [element * 2024]

def unorderedBlinkStash(list, blinks, height):
    for i in range(blinks % height):
        list = unorderedBlink(list)

    seen = {}
    new_list = []

    for i in range(0, blinks-height+1, height):
        print(f"done {i}/{blinks}")
        for element in list :
            if element in seen:
                new_list.extend(seen[element])
                continue
            values = multipleUnorderedBlink([element], height)
            new_list.extend(values)
            seen[element] = values
        list = new_list
        new_list = []
    return len(list)

def multipleUnorderedBlink(list, blinks):
    for i in range(blinks):
        list = unorderedBlink(list)
    return list
        
def unorderedBlink(list):
    new_list = []
    seen = {}
    for element in list:
        if element in seen:
            new_list.extend(seen[element])
            continue
        castedElement = str(element)
        length = len(castedElement)
        if element == 0:
            seen[0] = [1]
            new_list.append(1)
        elif length % 2 == 0:
            value1, value2 = int(castedElement[length//2:]) , int(castedElement[:length//2])
            seen[element] = [value1, value2]
            new_list.append(value1)
            new_list.append(value2)
        else:
            seen[element] = [element * 2024]
            new_list.append(element * 2024)
    return new_list

def count_stone_after_blink(list, blinks):
    for i in range(blinks):
        print(f"done {i}/{blinks}", end="\r")
        list = unorderedBlink(list)
    return len(list)