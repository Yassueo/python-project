a = []

import random

for i in range(10):
    a.append(random.randrange(1, 10))

for i in range(len(a)):
    print(a[i])
