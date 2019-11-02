#num_1과 num_2를 구한다
num_1 = int(input("num_1 >>>"))
num_2 = int(input("num_2 >>>"))
# 1 = +, 2 = -, 3 = *,4 = /,5 = %
Arithmetic_operation = int(input('Arithmetic operation(1,2,3,4,5)>>>'))  # type: int
if(Arithmetic_operation == 1):
    Calculation = num_1 + num_2
elif(Arithmetic_operation == 2):
    Calculation = num_1 - num_2
elif(Arithmetic_operation == 3):
    Calculation = num_1 * num_2
elif(Arithmetic_operation == 4):
    Calculation = num_1 / num_2
else:
    Calculation = num_1 % num_2
#구한값 출력하기
print(Calculation)
