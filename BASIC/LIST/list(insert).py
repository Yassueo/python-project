import random

a = []

for i in range(10):
    a.append(random.randrange(0,100))

a.insert(5 ,"hello")

print(a)