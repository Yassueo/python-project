from random import randrange
def make_list(some_num):
    for i in range(10):
        some_num.append(randrange(-100,100))
    return some_num
def judgment(temp,max):
    for i in range(1,len(some_num)):
        temp = temp + some_num[i]
        if temp > max:
            max = temp
        elif temp <= 0:
            temp = 0
    return max

max = 0
temp = 0
some_num = []

some_num = make_list(some_num)
max = judgment(temp,max)
print(some_num,'highest vaule is',max)
