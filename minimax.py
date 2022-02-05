import numpy as np
from math import inf


class MiniMax:
    """Class containing minimax algorithm functions and data"""
    def __init__(self, board):
        """Initializes the class with a board"""
        self.board = board

    def getMove(self, currentMove, nextMove):
        """Returns the best move for the current move token"""
        self.rootMove = currentMove  # stores the move to optimize

        self.winMoveDepth = inf  # worst case win scenario
        self.loseMoveDepth = 0  # worst case lose scenario

        # worst cast move value and location
        bestMoveValue, bestMoveLocation = -inf, None

        # iterates over each move
        for index, value in np.ndenumerate(self.board.cells):
            # checks if the move is in an empty space
            if self.board.cells[index] == "":
                # place the move
                self.board.placeMove(index, currentMove)

                # check for the winstate
                if self.board.checkWin(index):
                    return index

                # get the expected value of making the move
                val, moveDepth = self.minimax(
                    nextMove,
                    currentMove,
                    -inf,
                    inf
                )

                # restore the board state
                self.board.delMove(index)

                # if the move is an improvement on the best move so far
                if val >= bestMoveValue:
                    if val == -1 or val == 0:  # lose or draw
                        if moveDepth >= self.loseMoveDepth:
                            # prefer taking time to lose or draw
                            bestMoveValue = val
                            bestMoveLocation = index
                            self.loseMoveDepth = moveDepth
                    elif val == 1:  # win
                        if moveDepth < self.winMoveDepth:
                            # prefer to win quickly
                            bestMoveValue = val
                            bestMoveLocation = index
                            self.winMoveDepth = moveDepth
        return bestMoveLocation

    def minimax(self, currentMove, nextMove, alpha, beta):
        """Minimax function, including alpha beta pruning"""
        winMoveDepth = inf  # worst case win scenario
        loseMoveDepth = -1  # worst case lose scenario

        # check a draw state
        emptyCells = 0
        for index, value in np.ndenumerate(self.board.cells):
            if self.board.cells[index] == "":
                emptyCells += 1

        if emptyCells == 0:
            return 0, 0

        # worst case scenario
        bestMoveValue = -inf if currentMove == self.rootMove else inf

        # iterates over each move
        for index, value in np.ndenumerate(self.board.cells):
            # checks if the move is in an empty space
            if value == "":
                # place the move
                val, moveDepth = None, None
                self.board.placeMove(index, currentMove)

                # check for the winstate
                if self.board.checkWin(index):
                    moveDepth = 0

                    # positive value if AI wins, negative if player wins
                    val = 1 if currentMove == self.rootMove else -1
                else:
                    # recurse to get the expected value of making the move
                    val, moveDepth = self.minimax(
                        nextMove,
                        currentMove,
                        alpha,
                        beta
                    )

                # restore the board state
                self.board.delMove(index)

                if currentMove == self.rootMove:
                    # AI would be playing so prefer higher values
                    goodMove = (val >= bestMoveValue)
                else:
                    # human would be playing so prefer lower values
                    goodMove = (val <= bestMoveValue)

                # what is the ideal outcome for who/what plays this move
                targetOutcome = (1 if currentMove == self.rootMove else -1)

                # if the move is an improvement on the best move so far
                if goodMove:
                    if val == -targetOutcome or val == 0:  # lose or draw
                        if moveDepth >= loseMoveDepth:
                            # prefer taking time to lose or draw
                            bestMoveValue = val
                            loseMoveDepth = moveDepth
                            bestMoveDepth = moveDepth
                    elif val == targetOutcome:  # win
                        if moveDepth <= winMoveDepth:
                            # prefer to win quickly
                            bestMoveValue = val
                            winMoveDepth = moveDepth
                            bestMoveDepth = moveDepth

                # prune ineffectual branches
                if currentMove == self.rootMove:
                    alpha = max(alpha, bestMoveValue)
                else:
                    beta = min(beta, bestMoveValue)
                if alpha >= beta:
                    break
        return bestMoveValue, bestMoveDepth + 1
