import re
from minimax import MiniMax


class Multiplayer:
    def __init__(self, board):
        self.opponents = {
            1: PlayLocal(board),
            2: MiniMax(board),
        }
        self.board = board

    def getOpponent(self):
        print(
            "There are several opponents you can play against:\n",
            "1. Local multiplayer\n",
            "2. Against the computer\n",
            # "3. Against another player on the local network",
        )
        selection = ""
        while not re.match("^[1-3]$", selection):
            selection = input("Please enter the number of your selection:")
        return int(selection)

    def setOpponent(self, selection):
        self.opponent = self.opponents[selection]

    def getMove(self, currentMove, nextMove):
        return self.opponent.getMove(currentMove, nextMove)


class PlayLocal:
    def __init__(self, board):
        self.board = board

    def getMove(self, currentMove, nextMove):
        while 1:  # wait until valid move input
            inpt = input("Move: ")
            if re.match("^[0-2] [0-2]$", inpt):
                # turn text input to list of ints
                coordinate = [int(i) for i in inpt.split(" ")]

                # if the move is in an empty space, make it
                if self.board.placeMove(coordinate, currentMove):
                    return coordinate
