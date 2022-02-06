import numpy as np


class Board:
    """Class to contain functions and data related to a tic tac toe board"""
    def __init__(self):
        """Initialize class with blank board"""
        self.cells = np.zeros([3, 3], dtype="U3")
        self.lastMove = None

    def placeMove(self, coordinate, value):
        """Place a move with a token of value at the coordinate given"""
        # ensure the coordinate is a tuple, not a list
        coordinate = tuple(coordinate)

        # ensure the move is in an empty space
        if self.cells[coordinate] == "":
            self.cells.itemset(coordinate, f" {value} ")
            self.lastMove = coordinate
            return True
        return False

    def delMove(self, coordinate):
        """Clears a move from the board"""
        self.cells[coordinate] = ""

    def __repr__(self):
        """Return a string representing the board state"""
        return """
            +---+---+---+
            |{}|{}|{}|
            +---+---+---+
            |{}|{}|{}|
            +---+---+---+
            |{}|{}|{}|
            +---+---+---+""".format(*[
                                    value
                                    if value
                                    else "   "
                                    for value in np.nditer(self.cells)
                                    ])

    def checkWin(self, coordinate=None):
        """Check for a winstate caused by the given coordinate"""
        # if the coordinate to check is not given, check the last move
        coordinate = coordinate or self.lastMove

        # ensure the coordinate is a tuple, not a list
        coordinate = tuple(coordinate)

        # check the diagonal with the top left space
        if coordinate[0] == coordinate[1]:
            if all(
                self.cells[i, i] == self.cells[coordinate]
                for i in range(3)
            ):
                return True

        # check the diagonal with the top right space
        if coordinate[0] + coordinate[1] == 2:
            if all(
                self.cells[i, 2-i] == self.cells[coordinate]
                for i in range(3)
            ):
                return True

        # check the row
        if all(self.cells[
                coordinate[0],
                i
                ] == self.cells[coordinate]
                for i in range(0, 3)):
            return True

        # check the column
        if all(self.cells[
                i,
                coordinate[1]
                ] == self.cells[coordinate]
                for i in range(0, 3)):
            return True

        return False

    def clear(self):
        """Clears the board"""
        for index, value in np.ndenumerate(self.cells):
            self.delMove(index)
