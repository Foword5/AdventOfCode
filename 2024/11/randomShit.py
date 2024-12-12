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
        list = unorderedBlink(list)
    return len(list)


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

def multpileUnorderedBlink(list, blinks, seen = {}):
    for i in range(blinks):
        new_list = []
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
                if length < 15:
                    seen[element] = [value1, value2]
                new_list.append(value1)
                new_list.append(value2)
            else:
                if length < 15:
                    seen[element] = [element * 2024]
                new_list.append(element * 2024)
        list = new_list
    return list, seen

def unorderedBlinkStash(list, blinks, height):
    seen = {}
    for i in range(blinks % height):
        list, seen = multpileUnorderedBlink(list, 1, seen)

    new_list = []
    big_seen = {}

    for i in range(0, blinks-height+1, height):
        for element in list :
            if element in big_seen:
                new_list.extend(big_seen[element])
                continue
            values, seen = multpileUnorderedBlink([element], height, seen)
            new_list.extend(values)
            if len(str(element)) < 10:
                big_seen[element] = values
        list = new_list
        new_list = []
    return len(list)

if __name__ == "__main__" :
    list = [965842, 9159, 3372473, 311, 0, 6, 86213, 48]
    blinks = 25
    height = 5
    print(unorderedBlinkStash(list, blinks, height))
