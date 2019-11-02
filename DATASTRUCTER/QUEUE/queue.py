def enqueue(num):
    if len(queue) > max:
        print("overflow")
        return
    queue.append(num)
    return queue
def dequeue():
    if len(queue) == 0:
        print("underflow")
        return
    del queue[0]

max = 5
queue = []

while True:
    input_str = input('>>>')
    if input_str == "in":
        num = int(input('숫자를 입력해 주세요>>>'))
        queue = enqueue(num)
    elif input_str == "de":
        dequeue()
    elif input_str == "print":
        print(queue)
