# Dawson Merkle
# Project 1: Tic-Tac-Toe
# Implementing the MINMAX Adversarial Search Algorithm
# CAP4630
# 6/6/2023


import math

user = 'X'          # Setting the user to be the 'X' player
computer = 'O'      # Setting the AI to be the 'O' player


def printStartingBoard():       # Output the starting board with indexes for the user to use
    print('|' + ' 0 ' + '|' + ' 1 ' + '|' + ' 2 ' + '|')
    print('|' + ' 3 ' + '|' + ' 4 ' + '|' + ' 5 ' + '|')
    print('|' + ' 6 ' + '|' + ' 7 ' + '|' + ' 8 ' + '|')


def printBoard(board):      # Function used to print the board at any given state
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')


def makeMove(player, move, board):      # Function used to add a move to the board
    board[move] = player                # Adding the move to the board
    printBoard(board)                   # Printing the board after a new move
    if winner(board):                   # Checking to see if there is a winner with the new board
        print('\n' + player + ' has won the game.')     # Outputting the winner and ending the game
        return
    if draw(board):                     # Checking to see if there is a draw with the new board
        print('\n' + 'The game has ended in a draw.')   # Outputting a draw and ending the game
        return



def winner(board):      # Function used to check if there are any winners with the current board
    # Horizontal win
    if board[0] != ' ' and board[0] == board[1] and board[0] == board[2]:
        return True
    elif board[3] != ' ' and board[3] == board[4] and board[3] == board[5]:
        return True
    elif board[6] != ' ' and board[6] == board[7] and board[6] == board[8]:
        return True

    # Vertical win
    elif board[0] != ' ' and board[0] == board[3] and board[0] == board[6]:
        return True
    elif board[1] != ' ' and board[1] == board[4] and board[1] == board[7]:
        return True
    elif board[2] != ' ' and board[2] == board[5] and board[2] == board[8]:
        return True

    # Diagonal win
    elif board[0] != ' ' and board[0] == board[4] and board[0] == board[8]:
        return True
    elif board[2] != ' ' and board[2] == board[4] and board[2] == board[6]:
        return True

    # No winner
    else:
        return False


def findWinner(board, player):      # Function used to check if the passed player is the winner
    # Horizontal win
    if board[0] == player and board[0] == board[1] and board[0] == board[2]:
        return True
    elif board[3] == player and board[3] == board[4] and board[3] == board[5]:
        return True
    elif board[6] == player and board[6] == board[7] and board[6] == board[8]:
        return True

    # Vertical win
    elif board[0] == player and board[0] == board[3] and board[0] == board[6]:
        return True
    elif board[1] == player and board[1] == board[4] and board[1] == board[7]:
        return True
    elif board[2] == player and board[2] == board[5] and board[2] == board[8]:
        return True

    # Diagonal win
    elif board[0] == player and board[0] == board[4] and board[0] == board[8]:
        return True
    elif board[2] == player and board[2] == board[4] and board[2] == board[6]:
        return True

    # Player didn't win
    else:
        return False


def draw(board):                # Function used to check if there is a draw
    for v in range(9):          # Iterate through the whole board
        if board[v] == ' ':     # If there are any empty spaces then there is still more to be played
            return False
    return True                 # If there are no empty spaces then it's a draw


def computerMove(board):        # Function used to allow the AI to make a move on the board
    bestScore = -math.inf
    bestMove = 0
    for z in range(9):          # Iterate through all the empty slots on the board
        if board[z] == ' ':     # If empty space then set it to the computer's letter so that we can find the score
            board[z] = computer
            score = MINMAX(board, False, -math.inf, math.inf)        # Get the score for that potential move
            board[z] = ' '      # Undo the move so that we can try next potential move
            if score > bestScore:       # If the new score is better than we will make that move
                bestScore = score
                bestMove = z
    print("AI's turn, making a move now: ")
    makeMove(computer, bestMove, board)     # Make the AI's move using the best possible move from MINMAX



def MINMAX(board, min_or_max, alpha, beta):        # Function used to perform MinMax Algorithm
    if findWinner(board, computer):     # If the computer wins in the potential game (good)
        return 1
    elif findWinner(board, user):       # If the user wins in the potential game (bad)
        return -1
    elif draw(board):                   # If there is a draw in the potential game (fine)
        return 0

    if min_or_max:                              # Maximizing player
        bestScore = -math.inf
        for z in range(9):                      # Loop through the board
            if board[z] == ' ':                 # If empty space
                board[z] = computer             # Put a O
                score = MINMAX(board, False, alpha, beta)    # Recursive call with the new potential board
                board[z] = ' '                  # Undo the move
                if score > bestScore:           # If the new score is better than the best score make that move
                    bestScore = score
                    if bestScore >= alpha:      # Tree pruning
                        alpha = bestScore
            if alpha >= beta:
                break
        return bestScore
    else:                                       # Minimizing player
        bestScore = math.inf
        for z in range(9):                      # Loop through the board
            if board[z] == ' ':                 # If empty space
                board[z] = user                 # Put a X
                score = MINMAX(board, True, alpha, beta)     # Recursive call with the new potential board
                board[z] = ' '                  # Undo the move
                if score < bestScore:           # If the new score is better than the best score make that move
                    bestScore = score
                    if bestScore <= beta:       # Tree pruning
                        beta = bestScore
            if alpha >= beta:
                break
        return bestScore


def userMove(board):        # Function used to allow the user to make a move on the board
    move_index = 0          # Initialization of the index for the move
    valid_move = False      # Setting a flag to not allow the game to go on unless a valid input
    while not valid_move:
        move_index = input('It is your turn, choose your move (0-8): ')     # Ask the user to input move
        try:
            move_index = int(move_index)            # Try to set the input to an int (bail out if error)
            if move_index > 8 or move_index < 0:    # See if the int entered is within incorrect bounds
                raise ValueError                    # If it is then error
            if board[move_index] != ' ':            # If the board space isn't available then error
                raise ValueError
            valid_move = True                       # Tests passed, valid input, set flag to end while loop
        except ValueError:                          # Error catch that makes the user try again
            print('Not a number between 0-8 or that space is taken, try again.')
    makeMove(user, move_index, board)               # Make the move with the input given after validation


def main():

    playAgain = "Y"
    while playAgain == "Y" or playAgain == "y":     # While the player wants to play again

        win = False
        tie = False
        board = []  # Initialization of empty board to be used
        for x in range(9):
            board.append(' ')

        print("\nWelcome to TicTacToe! You are player 'X'")  # Welcome message for user
        printStartingBoard()  # Printing the starting board for the user to use

        while not win and not tie:                 # While loop that runs until there is a winner or draw
            print('\n')
            userMove(board)         # User goes first, then the AI
            computerMove(board)
            win = winner(board)     # Flag for winner
            tie = draw(board)       # Flag for draw
        playAgain = input('\nEnter Y if you would like to play again and anything else to exit: ')


if __name__ == '__main__':
    main()
