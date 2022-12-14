import time


tictac = [['_', '_', '_'],
          ['_', '_', '_'],
          ['_', '_', '_']]

def player1():
    row = int(input('Which row would you like to place \'X\' >'))
    col = int(input('Which column would you like to place \'X\' >'))
    if tictac[row - 1][col - 1] == '_':
        if row<4 and col<4 and row>0 and col>0:
            tictac[row - 1][col - 1] = 'X'
            game = str('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in tictac))
            print(game)
        else:
            print("INVALID INPUT: insert row values from 1 to 3 and column values from 1 to 3")
            print("START AGAIN")
    else:
        print("INVALID INPUT: You have inserted in a place occupied by player2")
        print("START AGAIN")


def player2():
    row = int(input('Which row would you like to place \'O\' >'))
    col = int(input('Which column would you like to place \'O\' >'))
    if tictac[row - 1][col - 1] == '_':
        if row<4 and col<4 and row>0 and col>0:
            tictac[row - 1][col - 1] = 'O'
            game = str('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in tictac))
            print(game)
        else:
            print("INVALID INPUT: insert row values from 1 to 3 and column values from 1 to 3")
            print("TRY AGAIN")
    else:
        print("INVALID INPUT: You have inserted in a place occupied by player1")
        print("START AGAIN")

def testing():
    #cases for player 1 winning
    if tictac[0][0] == 'X' and tictac[0][1] == 'X' and tictac[0][2] == 'X':
        print('PLAYER 1 WINS')
        exit()
    if tictac[1][0] == 'X' and tictac[1][1] == 'X' and tictac[1][2] == 'X':
        print('PLAYER 1 WINS')
        exit()
    if tictac[2][0] == 'X' and tictac[2][1] == 'X' and tictac[2][2] == 'X':
        print('PLAYER 1 WINS')
        exit()
    if tictac[0][0] == 'X' and tictac[1][0] == 'X' and tictac[2][0] == 'X':
        print('PLAYER 1 WINS')
        exit()
    if tictac[0][1] == 'X' and tictac[1][1] == 'X' and tictac[2][1] == 'X':
        print('PLAYER 1 WINS')
        exit()
    if tictac[0][2] == 'X' and tictac[1][2] == 'X' and tictac[2][2] == 'X':
        print('PLAYER 1 WINS')
        exit()
    if tictac[0][0] == 'X' and tictac[1][1] == 'X' and tictac[2][2] == 'X':
        print('PLAYER 1 WINS')
        exit()
    if tictac[0][2] == 'X' and tictac[1][1] == 'X' and tictac[2][0] == 'X':
        print('PLAYER 1 WINS')
        exit()

    #cases for player 2 winning
    if tictac[0][0] == 'O' and tictac[0][1] == 'O' and tictac[0][2] == 'O':
        print('PLAYER 2 WINS')
        exit()
    if tictac[1][0] == 'O' and tictac[1][1] == 'O' and tictac[1][2] == 'O':
        print('PLAYER 2 WINS')
        exit()
    if tictac[2][0] == 'O' and tictac[2][1] == 'O' and tictac[2][2] == 'O':
        print('PLAYER 2 WINS')
        exit()
    if tictac[0][0] == 'O' and tictac[1][0] == 'O' and tictac[2][0] == 'O':
        print('PLAYER 2 WINS')
        exit()
    if tictac[0][1] == 'O' and tictac[1][1] == 'O' and tictac[2][1] == 'O':
        print('PLAYER 2 WINS')
        exit()
    if tictac[0][2] == 'O' and tictac[1][2] == 'O' and tictac[2][2] == 'O':
        print('PLAYER 2 WINS')
        exit()
    if tictac[0][0] == 'O' and tictac[1][1] == 'O' and tictac[2][2] == 'O':
        print('PLAYER 2 WINS')
        exit()
    if tictac[0][2] == 'O' and tictac[1][1] == 'O' and tictac[2][0] == 'O':
        print('PLAYER 2 WINS')
        exit()


print('TIC TAC TOE GAME')
print('Take turns to insert \"X\"  and \"O\" as player one and player two respectively')
print('Insert letter in dimensions row 1 to 3 and column 1 to 3')
print(' ')

game = str('\n'.join('\t'.join('{:3}'.format(item) for item in row) for row in tictac))
print(game)
time.sleep(1)
print('   ')

print('Player 1\'s turn')
player1()
testing()
print('Player 2\'s turn')
player2()
testing()
print('Player 1\'s turn')
player1()
testing()
print('Player 2\'s turn')
player2()
testing()
print('Player 1\'s turn')
player1()
testing()
print('Player 2\'s turn')
player2()
testing()
print('Player 1\'s turn')
player1()
testing()
print('Player 2\'s turn')
player2()
testing()
print('Player 1\'s turn')
player1()
testing()


