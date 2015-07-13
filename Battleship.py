from random import randint

#holds values of board that have a battleship
spacesUsed = []
#size of board you want to play on
board_size = 10


for x in range(board_size):
    spacesUsed.append(["O"] * board_size)

class Battleship(object):
    sunk = False #whether battleship is sunk or not
    row = 0 #first row of ship
    col = 0 #first col of ship
    hit = 0 #keeps track of number of hits as user guesses
    def __init__(self, size, placement):
        self.size = size
        self.placement = placement
        self.spaces = [] #holds columns for horizontally placed ships and rows for vertically place ships
    
    def location(self, board): #place the ship on the board
        while True:
            row = randint(0, len(board) - 1)
            col = randint(0, len(board[0]) - 1)
            s = self.size
            if (self.placement == "h"): #check if ship can be placed horizontally here
                value = 0
                while s > 0:
                    if spacesUsed[row][col+value] == "X":
                        break #can't place ship here
                    value = value + 1
                    s = s - 1
            elif (self.placement == "v"): #check if ship can be placed vertically here
                value = 0
                while s > 0:
                    if spacesUsed[row+value][col] == "X":
                        break
                    value = value + 1
                    s = s - 1
            break
        self.row = row
        self.col = col
        s = self.size
        value = 0
        if (self.placement == "h"): #actually place ship to board
            while s > 0:
                spacesUsed[row][col+value] = "X"
                self.spaces.append(col+value)
                s = s - 1
                value = value + 1
        elif (self.placement == "v"):
            while s > 0:
                spacesUsed[row+value][col] = "X"
                self.spaces.append(col+value)
                s = s - 1
                value = value + 1
                
    def print_location(self): #print method for debugging
        print "(" + str(self.row) + ", " + str(self.col) + ")"
        for x in self.spaces:
            print x
				
board = []

    

for x in range(board_size):
    board.append(["O"] * board_size)

def print_board(board):
    for row in board:
        print " ".join(row)


print "Let's play Battleship!"
print_board(board)


    

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#create the battleships

ship1 = Battleship(2, "h") #v for vertical placement
ship1.location(board)
ship1.print_location()
ship2 = Battleship(1, "h") #h for horizontal placement
ship2.location(board)
ship2.print_location()


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship1.row: #since it is known ship1 is horizontally placed
        for s in ship1.spaces: 
            if s == guess_col: #checks if the user's guess col is one of the spaces of the ship location
                print "Congratulations! You hit my first battleship!"
                ship1.hit += 1
                break
        if ship1.hit == ship1.size:     #if num of hits on ship is equal to the size the ship is sunk
            ship1.sunk = True
            print "Congratulations! You sunk my first battleship!"
            
    elif guess_row == ship2.row: #since it is known ship2 is horizontally placed
        for s in ship2.spaces:
            if s == guess_col:
                print "Congratulations! You hit my second battleship!"
                ship2.hit += 1
                break
        if ship2.hit == ship2.size:
            ship2.sunk = True
            print "Congratulations! You sunk my second battleship!"
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
        else:
    # Print (turn + 1) here!
            print_board(board)
    if ship1.sunk == True and ship2.sunk == True:
        print "You win the game!"
        break