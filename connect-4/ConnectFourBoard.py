import copy

# Board tokens
RED = 1
BLUE = 2

# A few helper functions to manage board initialisation
def new_empty_board(height, width):
    return [([0] * height) for k in range(width)]

class InvalidBoard(Exception):
    pass

def valid_board(board):
    # Checks that the board is a rectangle. If it isn't, this function raises
    # an exception which interupts the program.
    if len(board) == 0:
        raise InvalidBoard('The board has no space')
    else:
        l = len(board[0])
        if any(len(col) != l for col in board):
            raise InvalidBoard('Not all columns have the same heights')
        elif l == 0:
            raise InvalidBoard('The board has no space')




class Board():

    def __init__(self, board=None, rewards=None, winscore=100):
        if board == None:
            # If no board is passed explicitely, just create one
            board = new_empty_board(9, 9)
        self.field = board
        # This next line will crash the program if the provided board is wrong
        valid_board(self.field)
        self.width = len(self.field)
        self.height = len(self.field[0])
        if rewards == None:
            # The default rewards: [0, 1, 2, 4, 8, 16, 32, etc. ]
            rewards = [0] + [ 2 ** (n - 1) for n in range(1, max(self.width, self.height)) ]
        rewards=[0, 1, 2, 4, 8, 16, 32, 64,128,256,512]
        #rewards=[0, 0, 0, 1, 1, 1, 1, 1,1,1,1]
        self.rewards = rewards
        self.winscore = winscore
        self.Test1=0
        self.Test2=0


    def copy(self):
        # Creates a new board using the same underlying field of play
        return Board(
             board=copy.deepcopy(self.field),
             rewards=self.rewards,
             winscore=self.winscore
        )

    def col_height(self, col):
        # Finds out the height of a given column
        # This is useful for inserting tokens and for detecting if the board
        # is full.
        l = 0
        if len(self.field[col])>0:
            for space in self.field[col]:
                if space != 0:
                    l += 1
        return l

    def not_full_columns(self):
        # This method collects all the columns that are not full. This gives a
        # list of playable columns. It is useful for AIs.
        cs = []
        for col in range(self.width):
            if self.col_height(col) < self.height:
                cs.append(col)
        return cs

    def attempt_insert(self, col, token):
        # is it possible to insert into this column?
        if self.col_height(col) < self.height:

            # add a token in the selected column
            self.field[col][self.col_height(col)] = token
            # return True for success
            return True

        else:
            # return False for Failure
            return False
    def score(self):
        red = 0
        blue = 0
        scoring=0
        temp=1
        for x in range(len(self.field)):
            for y in range(len(self.field[0])):
                if scoring==0:
                    if (self.field[x][y])!=0:
                        scoring=self.field[x][y]
                        temp=1
                else:
                    if scoring==self.field[x][y]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (self.field[x][y])!=0:
                            scoring=self.field[x][y]
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
        scoring=0
        temp=1
        for x in range(len(self.field[0])):
            for y in range(len(self.field)):
                if scoring==0:
                    if (self.field[y][x])!=0:
                        scoring=self.field[y][x]
                        temp=1
                else:
                    if scoring==self.field[y][x]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (self.field[y][x])!=0:
                            scoring=self.field[y][x]
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
        scoring=0
        temp=1
        Done=False
        startX=0
        startY=len(self.field[0])-1
        lengthofdiag=1
        while not Done:
            x=startX
            y=startY
            for i in range(lengthofdiag):
                if scoring==0:
                    if (self.field[y][x])!=0:
                        scoring=self.field[y][x]
                        temp=1
                else:
                    if scoring==self.field[y][x]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (self.field[y][x])!=0:
                            scoring=self.field[y][x]
                x+=1
                y+=1
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
            if startY<1:
                if startX<len(self.field[0])-1:
                    startY=0
                    startX+=1
                    lengthofdiag-=1
                else:
                    Done=1
            else:
                startY-=1
                lengthofdiag+=1
        Done=False
        startX=len(self.field[0])-1
        startY=len(self.field)-1
        lengthofdiag=1
        while not Done:
            x=startX
            y=startY
            for i in range(lengthofdiag):
                if scoring==0:
                    if (self.field[y][x])!=0:
                        scoring=self.field[y][x]
                        temp=1
                else:
                    if scoring==self.field[y][x]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (self.field[y][x])!=0:
                            scoring=self.field[y][x]
                x-=1
                y+=1
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
            if startY<1:
                if startX>0:
                    startY=0
                    startX-=1
                    lengthofdiag-=1
                else:
                    Done=1
            else:
                startY-=1
                lengthofdiag+=1
        return (red, blue)
    def scoreAITEMP(self, field):
        red = 0
        blue = 0
        scoring=0
        temp=1
        for x in range(len(field)):
            for y in range(len(field[0])):
                if scoring==0:
                    if (field[x][y])!=0:
                        scoring=field[x][y]
                        temp=1
                else:
                    if scoring==field[x][y]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (field[x][y])!=0:
                            scoring=field[x][y]
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
        scoring=0
        temp=1
        for x in range(len(field[0])):
            for y in range(len(field)):
                if scoring==0:
                    if (field[y][x])!=0:
                        scoring=field[y][x]
                        temp=1
                else:
                    if scoring==field[y][x]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (field[y][x])!=0:
                            scoring=field[y][x]
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
        scoring=0
        temp=1
        Done=False
        startX=0
        startY=len(field[0])-1
        lengthofdiag=1
        while not Done:
            x=startX
            y=startY
            for i in range(lengthofdiag):
                if scoring==0:
                    if (field[y][x])!=0:
                        scoring=field[y][x]
                        temp=1
                else:
                    if scoring==field[y][x]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (field[y][x])!=0:
                            scoring=field[y][x]
                x+=1
                y+=1
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
            if startY<1:
                if startX<len(field[0])-1:
                    startY=0
                    startX+=1
                    lengthofdiag-=1
                else:
                    Done=1
            else:
                startY-=1
                lengthofdiag+=1
        Done=False
        startX=len(field[0])-1
        startY=len(field)-1
        lengthofdiag=1
        while not Done:
            x=startX
            y=startY
            for i in range(lengthofdiag):
                if scoring==0:
                    if (field[y][x])!=0:
                        scoring=field[y][x]
                        temp=1
                else:
                    if scoring==field[y][x]:
                        temp+=1
                    else:
                        if scoring==1:
                            red+=int(self.rewards[temp-1])
                            scoring=0
                        elif scoring==2:
                            blue+=int(self.rewards[temp-1])
                            scoring=0
                        temp=1
                        if (field[y][x])!=0:
                            scoring=field[y][x]
                x-=1
                y+=1
            if scoring==1:
                red+=int(self.rewards[temp-1])
            elif scoring==2:
                blue+=int(self.rewards[temp-1])
            scoring=0
            temp=1
            if startY<1:
                if startX>0:
                    startY=0
                    startX-=1
                    lengthofdiag-=1
                else:
                    Done=1
            else:
                startY-=1
                lengthofdiag+=1
        return (red, blue)
    def CheckColumns():
        pass


    def is_full(self):
        Full=True
        for x in len(self.field[0]):
            for y in len(self.field):
                if self.field[x][y]==0:
                    Full=False
        return Full




# This additional class simply creates an empty board of a given size.
# Note the `Board` between brackets (`(` and `)`). This means that the methods
# from the class `Board` are available in the class `EmptyBoard`. In other
# words, `EmptyBoard` is just a special case of the general case `Board`.
class EmptyBoard(Board):

    # Function to set up the objects of this class
    def __init__(self, height=8, width=9, rewards=None, winscore=100):
        # Create a simple empty board with the right height and width
        fresh_board = new_empty_board(height, width)
        # Then, proceed to set-up as in `Board`. The `super()` part refers to
        # the class `Board`.
        Board.__init__(self, fresh_board, rewards, winscore)
