def list_from_file(file_path):
    list = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            list.append([int(item) for item in line.split(' ')])
    return list

def report_is_safe(report):
    increasing = report[0] < report[1]
    for i in range(len(report)-1):
        next_element = report[i+1]
        if increasing and report[i] > next_element:
            return False
        elif not increasing and report[i] < next_element:
            return False
        if abs(report[i] - next_element) < 1 or abs(report[i] - next_element) > 3:
            return False
    return True

def try_with_all(report):
    for i in range(len(report)):
        copy = report.copy()
        del copy[i]
        if report_is_safe(copy):
            return True
    return False

def report_is_safe_using_dampener(report):
    increasing = report[0] < report[1]
    if increasing and report[1] > report[2] and report[2] > report[3]:
        increasing = False
    elif not increasing and report[1] < report[2] and report[2] < report[3]:
        increasing = True
    for i in range(len(report)-1):
        next_element = report[i+1]
        if increasing and report[i] > next_element:
            copy = report.copy()
            del report[i]
            del copy[i+1]
            return report_is_safe(report) or report_is_safe(copy)
        elif not increasing and report[i] < next_element:
            copy = report.copy()
            del report[i]
            del copy[i+1]
            return report_is_safe(report) or report_is_safe(copy)
        if abs(report[i] - next_element) < 1 or abs(report[i] - next_element) > 3:
            copy = report.copy()
            del report[i]
            del copy[i+1]
            return report_is_safe(report) or report_is_safe(copy)
    return True

def nbr_of_safe_reports(list):
    count = 0
    for report in list:
        if report_is_safe(report):
            count += 1
    return count

def nbr_of_safe_reports_using_dampener(list):
    count = 0
    for report in list:
        if report_is_safe_using_dampener(report):
            count += 1
    return count

if __name__ == "__main__":
    list = list_from_file("input.txt")
    print(nbr_of_safe_reports_using_dampener(list))