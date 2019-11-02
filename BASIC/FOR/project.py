temp = str(input("We combine letter>>>")).upper()
combine = []
word_list = ['C','A','M','B',"R",'I','D','G','E']
repeat = 0
flag = 0

if len(temp) <= 2 or len(temp) >= 100 :
    print('plz enter over 3 and under 100')

for i in range(len(temp)):
    flag = 0
    for j in range(len(word_list)):
        if word_list[j] == temp[i]:
            flag = 1

    if flag == 0:
        combine.append(temp[i])

print(combine)