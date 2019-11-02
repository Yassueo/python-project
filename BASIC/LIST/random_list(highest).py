a = []
import random

for i in range(10):
    a.append(random.randrange(1,100))

highest = a[0]
lowest = a[0]
for j in range(len(a)):
    if highest < a[j]:
        highest = a[j]
    if lowest > a[j]:
        lowest = a[j]
print(a)
print("highest number is", highest)
print("lowest number is ", lowest)
