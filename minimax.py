import numpy as np
from math import inf
from functools import lru_cache


class MiniMax:
    def __init__(self, board):
        self.board = board

    def getMove(self, currentMove, nextMove):
        self.rootMove = currentMove  # stores the move to optimize
        self.maxDepth = -1
        for index, value in np.ndenumerate(self.board.cells):
            if self.board.cells[index] == "":
                self.maxDepth += 1

        self.winMoveDepth = self.maxDepth  # worst case win scenario
        self.loseMoveDepth = 0  # worst case lose scenario

        # worst cast move value and location
        bestMoveValue, bestMoveLocation = -inf, None

        for index, value in np.ndenumerate(self.board.cells):
            if self.board.cells[index] == "":
                self.board.placeMove(index, currentMove)
                if self.board.checkWin(index):
                    return index
                val, moveDepth = self.minimax(
                    self.maxDepth,
                    nextMove,
                    currentMove,
                    -inf,
                    inf
                )
                self.board.delMove(index)

                if val >= bestMoveValue:
                    if val == -1 or val == 0:
                        if moveDepth >= self.loseMoveDepth:
                            bestMoveValue = val
                            bestMoveLocation = index
                            self.loseMoveDepth = moveDepth
                    elif val == 1:
                        if moveDepth < self.winMoveDepth:
                            bestMoveValue = val
                            bestMoveLocation = index
                            self.winMoveDepth = moveDepth
                # print(index, val, moveDepth)
        return bestMoveLocation

    def minimax(self, depth, currentMove, nextMove, alpha, beta):
        winMoveDepth = self.maxDepth+1  # worst case win scenario
        loseMoveDepth = -1  # worst case lose scenario

        emptyCells = 0
        for index, value in np.ndenumerate(self.board.cells):
            if self.board.cells[index] == "":
                emptyCells += 1

        if emptyCells == 0:
            return 0, 0

        bestMoveValue = -inf if currentMove == self.rootMove else inf

        for index, value in np.ndenumerate(self.board.cells):
            if value == "":
                val, moveDepth = None, None
                self.board.placeMove(index, currentMove)
                if self.board.checkWin(index):
                    moveDepth = 0
                    val = 1 if currentMove == self.rootMove else -1
                else:
                    val, moveDepth = self.minimax(
                        depth-1,
                        nextMove,
                        currentMove,
                        alpha,
                        beta
                    )
                self.board.delMove(index)

                if currentMove == self.rootMove:
                    goodMove = (val >= bestMoveValue)
                else:
                    goodMove = (val <= bestMoveValue)
                targetOutcome = (1 if currentMove == self.rootMove else -1)

                if goodMove:
                    if val == -targetOutcome or val == 0:
                        if moveDepth >= loseMoveDepth:
                            bestMoveValue = val
                            loseMoveDepth = moveDepth
                            bestMoveDepth = moveDepth
                    elif val == targetOutcome:
                        if moveDepth <= winMoveDepth:
                            bestMoveValue = val
                            winMoveDepth = moveDepth
                            bestMoveDepth = moveDepth
                if currentMove == self.rootMove:
                    alpha = max(alpha, bestMoveValue)
                else:
                    beta = min(beta, bestMoveValue)
                if alpha >= beta:
                    break
        return bestMoveValue, bestMoveDepth + 1
