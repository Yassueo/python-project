a = int(input("first Greatest common divisor >>> "))
b = int(input("second Greatest common divisor >>> "))
temp = []
temp_2 = []
counter = 0
Greatest_common_divisor = 0

for i in range(1,a + 1):
    if a % i == 0:
        temp.append(i)
        
for i in range(1,b + 1):
    if b % i == 0:
      temp_2.append(i)

if len(temp) < len(temp_2):
    for i in range(len(temp)):
        counter = counter + 1
        for i in range(len(temp)):
            if temp_2[counter] < temp[i]:
                Greatest_common_divisor = i

elif len(temp_2) > len(temp):
    for i in range(len(temp_2)):
        counter = counter + 1
        for i in range(len(temp_2)):
            if temp[counter] < temp_2[i]:
                Greatest_common_divisor = i


print(Greatest_common_divisor, "is", a, "and", b, "'s Greatest_common_divisor")
