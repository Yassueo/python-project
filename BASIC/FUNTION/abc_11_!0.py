x = 0

def plus(x,d):
    if (d[1] == '+'):
        x = int(d[0]) + int(d[2])

    print(x)

def minus(x,d):
    if (d[1] == '-'):
        x = int(d[0]) - int(d[2])
    print(x)

def multiplication(x,d):
    if (d[1] == '*'):
        x = int(d[0]) * int(d[2])
    print(x)

def division(x,d):
    if (d[1] == '/'):
        x = int(d[0]) / int(d[2])
    print(x)

c = -1

def push(a,stack,max,c):

    if(c == max):
        print('error')
        return c,stack
    stack.append(a)
    c = c + 1
    return c,stack

d = []
def pop(stack,c):
    if(c == -1):
        print('error')
        return
    d.append(stack[c])
    del stack[c]
    print(stack)
    c = c - 1
    return c,stack,d

stack = []
max = 10

while(1):
    data = input()

    if(data == 0):
        break

    elif(data == 1):
        a = input()
        c,stack = push(a,stack,max,c)
        print(stack)
    else:
        c,stack,d = pop(stack,c)
        print(d)

plus(x,d)

minus(x,d)

multiplication(x,d,)

division(x,d)
