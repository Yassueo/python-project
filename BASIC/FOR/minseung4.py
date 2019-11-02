
a = int(input())
b = 0

for i in range(2, int(a/2)+1):
    if(a%i == 0):
        b = 1
        break

if(b == 0):
    print("prime")
else:
    print("not prime")










