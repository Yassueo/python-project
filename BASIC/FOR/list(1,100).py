a = []
answer = 2
for i in range(1,101):
    a.append(i)

input_a = int(input("Enter the number >>> "))

start = 1
end = 100

for i in range(end):
    mid = int(start + end / 2)
    if mid == input_a:
        answer = mid
        break
    elif mid > input_a:
        end = mid
        print(mid)
    # mid < input_a
    else:
        start = mid
        print(mid)

answer = mid
print(answer)

