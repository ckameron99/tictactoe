import numpy as np


class Board:
    def __init__(self):
        self.cells = np.zeros([3, 3], dtype="U3")

    def placeMove(self, coordinate, value):
        coordinate = tuple(coordinate)
        if self.cells[coordinate] == "":
            self.cells.itemset(coordinate, f" {value} ")
            return True
        return False

    def delMove(self, coordinate):
        self.cells[coordinate] = ""

    def __repr__(self):
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

    def checkWin(self, coordinate):
        coordinate = tuple(coordinate)
        if coordinate[0] == coordinate[1]:
            if all(
                self.cells[i, i] == self.cells[coordinate]
                for i in range(3)
            ):
                return True

        if coordinate[0] + coordinate[1] == 2:
            if all(
                self.cells[i, 2-i] == self.cells[coordinate]
                for i in range(3)
            ):
                return True

        if all(self.cells[
                coordinate[0],
                i
                ] == self.cells[coordinate]
                for i in range(0, 3)):
            return True

        if all(self.cells[
                i,
                coordinate[1]
                ] == self.cells[coordinate]
                for i in range(0, 3)):
            return True

        return False
