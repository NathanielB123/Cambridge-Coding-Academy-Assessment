import random
import ConnectFourBoard
def AIcheck(board, token):  # randomly select a column
    available_moves = board.not_full_columns()
    if board.Test2==0:
        if board.Test1==0 or board.Test1==8:
            board.Test1=random.choice(available_moves)
        else:
            board.Test1+=random.randint(-1,1)
        board.Test2=random.randint(2,4)
    else:
        board.Test2-=1
    if board.Test2 in board.not_full_columns():
        print("OK")
        return board.Test1
    else:
        print("YAY")
        board.Test1=random.choice(available_moves)
        return board.Test1
