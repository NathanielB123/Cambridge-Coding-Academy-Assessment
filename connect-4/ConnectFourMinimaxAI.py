import copy
import ConnectFourBoard
import ConnectFourEngine
import random

def other(token):
    if token == ConnectFourBoard.RED:
        return ConnectFourBoard.BLUE
    elif token == ConnectFourBoard.BLUE:
        return ConnectFourBoard.RED
    else:
        return None


# estimate of a field quality
def state_score(game, token,field):
    import random
    score_red, score_blue = game.scoreAITEMP(field)
    return (score_red-(score_blue)+(random.randint(-4,4)/10)) #Returns the score with a little randomness to make games not always play out the same way

def max_play(board, token,newfield, remaining_ply, fieldheights):
    moves = []
    for n in range(0, board.width):
        if (fieldheights[n] < board.height):
            newfield = copy.deepcopy(newfield)
            newheights = copy.deepcopy(fieldheights)
            token = 1 if token else 2
            newfield[n][newheights[n]] = token
            newheights[n] += 1
            if remaining_ply <= 0:
                value = state_score(board,token, newfield)
            else:
                (min_move, value) = min_play(board,token, newfield, newheights, remaining_ply-1)
            moves.append([n,value])
    if len(moves)>0:
        return max(moves, key = lambda x: x[1])
    else:
        return [board.not_full_columns(),random.randint(1,3)]

def min_play(board,token, field, fieldheights,remaining_ply):
    moves = []
    for n in range(0, board.width):
        if (fieldheights[n] < board.height):
            newfield = copy.deepcopy(field)
            newheights = copy.deepcopy(fieldheights)
            # Notice the opposite turn here
            token = 2 if token else 1
            newfield[n][newheights[n]] = token
            newheights[n] += 1
            if remaining_ply <= 0:
                value = state_score(board,token, newfield)
            else:
                (min_move, value) = max_play(board,token, newfield, remaining_ply-1,newheights)
            moves.append([n,value])
    # This best move for Min finds the minimum board value
    if len(moves)>0:
        return min(moves, key = lambda x: x[1])
    else:
        return [board.not_full_columns(),random.randint(1,3)]

def AIcheck(board, token):
    import time
    ST=time.time()
    ply_remaining = 1
    fieldheights=[]
    field=board.field
    for i in range(board.width):
        fieldheights.append(board.col_height(i))
    (move, value) = max_play(board, token,field, ply_remaining, fieldheights)
    print("M"+str(time.time()-ST))
    return move
