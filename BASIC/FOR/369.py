
i = 0
for i in range(1, 100):
    f_num = int(i % 10)
    s_num = int(i / 10)
    if f_num == 3 or f_num == 6 or f_num == 9:
        if s_num == 3 or s_num == 6 or s_num == 9:
            print("**")
        else:
            print("*")
    elif s_num == 3 or s_num == 6 or s_num == 9:
            print("*")
    else:
        print(i)
