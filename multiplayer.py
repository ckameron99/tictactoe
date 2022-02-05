import re
from minimax import MiniMax


class Multiplayer:
    """Class to store functions and data relating to players"""
    def __init__(self, board):
        """Initializes the multiplayer class"""
        # define possible opponents
        self.opponents = {
            1: PlayLocal(board),
            2: MiniMax(board),
        }
        self.board = board

    def getOpponent(self):
        """Get's the user's choice of opponent"""
        print(
            "There are several opponents you can play against:\n",
            "1. Local multiplayer\n",
            "2. Against the computer\n",
            # "3. Against another player on the local network",
        )

        # get user selection
        selection = ""
        while not re.match("^[1-2]$", selection):  # TODO network option
            selection = input("Please enter the number of your selection:")
        return int(selection)

    def setOpponent(self, selection):
        """Set the choice of opponent"""
        self.opponent = self.opponents[selection]

    def getMove(self, currentMove, nextMove):
        """Returns the player's desired move"""
        return self.opponent.getMove(currentMove, nextMove)


class PlayLocal:
    """Class to store functions and data relating to a local player"""
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
