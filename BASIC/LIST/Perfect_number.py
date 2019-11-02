def make_list():
    for i in range(input_a):
        if i != 0 and input_a % i == 0:
            list_perfect_num.append(i)
    return list_perfect_num
def calculate(perfect_num):
    for i in range(len(list_perfect_num)):
        perfect_num = perfect_num + list_perfect_num[i]
    return perfect_num

def Judgment(perfect_num):
    if input_a == perfect_num:
        print('perfect number')
    else:
        print("not perfect number")
    return

list_perfect_num = []
input_a = int(input(">>>"))
perfect_num = 0

list_perfect_num = make_list()
perfect_num = calculate(perfect_num)
flag = Judgment(perfect_num)
