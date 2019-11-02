
def plus(a, b):
    c = a + b
    return c

def minus(a, b):
    c = a - b
    return c

def multiply(a, b):
    c = a * b
    return c

def division(a, b):
    c = a /b
    return c

print('get number arithmetic')
a = int(input('>>>'))
b = float(input('>>>'))
arithmetic = int(input('>>>'))
if arithmetic == 1:
    print(plus(a,b))
elif arithmetic == 2:
    print(minus(a,b))
elif arithmetic == 3:
    print(multiply(a,b))
else:
    print(division(a,b))

