m = int(input('m is? >>>'))
n = int(input('n is? >>>'))
all = 0

for i in range(m,n):
    temp = i * i
    all = all + temp

print(all)