start = 1
end = 100


b = int(input())
for i in range(101):
    middle=(int(start+end)/2)

    if (b == middle):
        print("find")

        break
    elif(b<middle):
        end=middle
    else:
        start=middle

#binary_serach




