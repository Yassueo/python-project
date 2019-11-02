a = input("first Greatest common divisor >>> ")
b = input("first Greatest common divisor >>> ")
temp = 0
max = 0

if a > b:
    temp = a
else:
    temp = b

for i in range(1, temp + 1):
    if a % i == 0 and b % i == 0:
        max = i

print(max)
