def push(list_stack):
    if len(list_stack) >= max:
        print("overflow")
        return list_stack
    list_stack.append(randrange(1, 100))
    print(list_stack)
    return list_stack

def pop(list_stack):
    if len(list_stack) == 0:
        print("underflow")
        return list_stack
    del list_stack[len(list_stack) - 1]
    print(list_stack)
    return list_stack

from random import randrange
max = 5
list_stack = []

while True:
    input_a = input('>>>')

    if input_a =="push":
        list_stack = push(list_stack)
    elif input_a == "pop":
        list_stack = pop(list_stack)
    elif input_a == 'break':
         break
