a = []
k = 0
import random

for i in range(10):
    flag = 0
    k = random.randrange(1,100)

    for j in range(len(a)):
        if k == a[j]:
            flag = 1
            break

    if flag == 0:
        a.append(k)

print(a)