prime = int(input(">>>"))
flag = True
for i in range(2, int(prime/2)+1):
    if prime % i == 0:
        flag = False
        break

if flag:
    print(prime,"is prime")
else:
    print(prime,"isn't prime")
