


def make_list():
    list_temp = []
    for i in range(8):
        list_temp.append(int(input(">>>")))
    return list_temp
def check_highest(list_temp):
    highest = []
    for j in range(5):
        temp = 0
        for i in range(len(list_temp)):
            if list_temp[temp] < list_temp[i]:
                temp = i
        highest.append([list_temp[temp], temp])
        list_temp[temp] = -1
    return highest


def total_plus(highest):
    total = []
    for i in range(len(highest)):
        total += highest[i][0]
    return highest
def print_print(highest):
    print(total)
    for i in range(len(highest)):
        print(highest[i][1])

list_temp = make_list()
highest = check_highest()
total_plus(highest)
print_print(highest)
