from random import randrange
max = 5
list_stack = []

while True:
    input_a = input('>>>')

    if input_a == "push":
        if len(list_stack) > max:
            print("overflow")
            continue
        list_stack.append(randrange(1,100))
        print(list_stack)
    elif input_a == "pop":
        if len(list_stack) == 0:
            print("underflow")
            continue
        del list_stack[len(list_stack)-1]
        print(list_stack)

    elif input_a == "break":
        break

