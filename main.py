from board import Board
from minimax import MiniMax
import os
import re
import time


def main():
    # welcome splash
    clearTerminal()
    welcome()
    # clear splash, initialize the board
    clearTerminal()
    board = Board()
    movesMade = 0

    # display the board to the user
    print(board)

    # define the moveset
    currentMove, nextMove = "X", "O"

    # initialize an ai opponent
    ai = MiniMax(board)

    # main game loop
    while True:
        while 1:  # wait until valid move input
            inpt = input("Move: ")
            if re.match("^[0-2] [0-2]$", inpt):
                # turn text input to list of ints
                coordinate = [int(i) for i in inpt.split(" ")]

                # if the move is in an empty space, make it
                if board.placeMove(coordinate, currentMove):
                    movesMade += 1
                    break
        
        # update the board view
        clearTerminal()
        print(board)

        # check the board for endstates
        if board.checkWin(coordinate):
            input(f"{currentMove} has won!")
            exit()
        if movesMade == 9:
            input("Draw!")
            exit()

        # play the AI's move
        t1 = time.perf_counter()
        coordinate = ai.getMove(nextMove, currentMove)
        t2 = time.perf_counter()
        board.placeMove(coordinate, nextMove)
        movesMade += 1

        # update the board view
        clearTerminal()
        print(board)
        print(t2-t1)



        if board.checkWin(coordinate):
            input(f"{nextMove} has won!")
            exit()
        if movesMade == 9:
            input("Draw!")
            exit()


def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def welcome():
    input(
        "Welcome to tictactoe, place three of your tokens in a row to win!\n"
        "You can place a token by entering two numbers separated by a space,"
        " the first is how many from the top row it is, the second is how "
        "many along from the left row it is.\n"
        "For example, if you want to place a token in the middle right square,"
        " enter \"1 2\"\n"
        "Press Enter to continue."
    )


if __name__ == "__main__":
    main()
