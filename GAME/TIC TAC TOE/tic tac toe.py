import random as r

def select_mark():
    user_mark = str(input("choose your mark>>>(x,o)")).lower()
    if user_mark == 'x':
        return 'x','o'
    elif user_mark == 'o':
        return 'o','x'
    else:
        while not (user_mark == 'x' or uesr_mark == 'o'):
            uesr_mark = str(input("choose your mark>>>(x,o)"))
# make random order (1 = com,0 = user)
def random_order():
    order = r.randrange(0,2)
    if order == 1:
        return 1
    elif order == 0:
        return 0
#make game board
def make_board():
    board = []
    for i in range(9):
        board.append("*")
    return board

def check_win(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return 'win'
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        return 'win'
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        return 'win'
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return 'win'
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return 'win'
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        return 'win'
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        return 'win'
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        return 'win'
    else:
        return "lose"

def print_board(board):
    for i in range(3):
            print(board[i])

board = make_board()
print_board(board)
