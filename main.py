from board import Board
from multiplayer import Multiplayer, PlayLocal
import os


def main():
    """Main program function"""
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

    # initialize local player
    localPlayer = PlayLocal(board)

    # initialize an opponent
    opponent = Multiplayer(board)
    choice = opponent.getOpponent()
    opponent.setOpponent(choice)

    currentPlayer, nextPlayer = localPlayer, opponent

    # main game loop
    while True:
        # play the current player's move
        coordinate = currentPlayer.getMove(currentMove, nextMove)
        board.placeMove(coordinate, currentMove)
        movesMade += 1

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

        # change player
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
        currentMove, nextMove = nextMove, currentMove


def clearTerminal():
    """OS independent terminal clearing"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def welcome():
    """Waits for confirmation after displaying welcome message"""
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
