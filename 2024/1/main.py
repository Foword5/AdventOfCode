def list_from_file(file):
    list1 = []
    list2 = []
    with open(file, 'r') as f:
        for line in f:
            splited_line = line.split(" ")
            list1.append(splited_line[0])
            list2.append(splited_line[3].split("\n")[0])
    return list1, list2

def calculate_distance(list1, list2):
    list1.sort()
    list2.sort()
    if len(list1) != len(list2):
        return -1
    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))
    return distance

def calculate_similarity_score(list1, list2):
    sim = 0
    for i in range(len(list1)):
        small_sim = 0
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                small_sim += 1
        sim += int(list1[i]) * small_sim
    return sim

if __name__ == "__main__":
    list1, list2 = list_from_file("input.txt")
    print(calculate_similarity_score(list1, list2))