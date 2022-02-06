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

        # get the location of the best move
        val, moveDepth, bestMoveLocation, = self.minimax(
            currentMove,
            nextMove,
            -inf,
            inf,
            rootNode=True
        )
        return bestMoveLocation

    def minimax(self, currentMove, nextMove, alpha, beta, rootNode=False):
        """Minimax function, including alpha beta pruning"""
        winMoveDepth = inf  # worst case win scenario
        loseMoveDepth = 0  # worst case lose scenario

        # check a draw state
        emptyCells = 0
        for index, value in np.ndenumerate(self.board.cells):
            if self.board.cells[index] == "":
                emptyCells += 1

        if emptyCells == 0:
            return 0, 0, None

        # worst case scenario
        bestMoveValue = -inf if currentMove == self.rootMove else inf
        bestMoveLocation = None

        # iterates over each move
        for index, value in np.ndenumerate(self.board.cells):
            # checks if the move is in an empty space
            if value == "":
                # place the move
                # val, moveDepth = None, None
                self.board.placeMove(index, currentMove)

                # check for the winstate
                if self.board.checkWin():
                    moveDepth = 0

                    # positive value if AI wins, negative if player wins
                    val = 1 if currentMove == self.rootMove else -1
                    self.board.delMove(index)
                    return val, 1, index
                else:
                    # recurse to get the expected value of making the move
                    val, moveDepth, null = self.minimax(
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
                            bestMoveLocation = index
                    elif val == targetOutcome:  # win
                        if moveDepth <= winMoveDepth:
                            # prefer to win quickly
                            bestMoveValue = val
                            winMoveDepth = moveDepth
                            bestMoveDepth = moveDepth
                            bestMoveLocation = index

                # root nodes must not be pruned
                if not rootNode:
                    # prune ineffectual branches
                    if alpha >= beta:
                        break
                    if currentMove == self.rootMove:
                        alpha = max(alpha, bestMoveValue)
                    else:
                        beta = min(beta, bestMoveValue)

        return bestMoveValue, bestMoveDepth + 1, bestMoveLocation
