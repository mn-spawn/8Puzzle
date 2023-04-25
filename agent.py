from __future__ import annotations
from board import Board
from collections.abc import Callable
import numpy as np


'''
Heuristics
'''
def MT(board: Board) -> int:
    '''
    Compare the current board to the correct board and see how many
    mismatched tiles you have (misplaced tiles)
    '''

    correctboard = ([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]])

    b = board.state

    misplacedtiles= 0
    for row in range(3):
        for column in range(3):
            if b[row][column] != correctboard[row][column]:
                misplacedtiles +=1
        

    return misplacedtiles

def CB(board: Board) -> int:
    '''
    For each block in the given Board get the city block distance
    and sum to the total city block distance
    '''
    totalcbd = 0
    b = board.state

    for row in range(3):
        for column in range(3):
            tilecbd = 0

            tilecbd = getElement(b[row][column], row, column)
            totalcbd += tilecbd

    return totalcbd

def NA(board: Board) -> int:
    #my heuristic here
    print("NA")
    return 0

def getElement(num, row, col):
    ''' 
    Helper function that takes in the number and outputs it's city block
    distance from where it should be
    '''

    if num == 1: return (abs(0-row) + abs(0-col))
    elif num == 2: return (abs(0-row) + abs(1-col))
    elif num == 3: return (abs(0-row) + abs(2-col))
    elif num == 4: return (abs(1-row) + abs(0-col))
    elif num == 5: return (abs(1-row) + abs(1-col))
    elif num == 6: return (abs(1-row) + abs(2-col))
    elif num == 7: return (abs(2-row) + abs(0-col))
    elif num == 8: return (abs(2-row) + abs(1-col))
    elif num == 0: return (abs(2-row) + abs(2-col))


'''
A* Search 
'''

def a_star_search(board: Board, heuristic: Callable[[Board], int]):

    solution = []
    found = False 
    
    closedcases = [board]
    limit = 0
    gscore = 0

    while not found and limit != 10:
        # if we found our goal state return 
        if board.goal_test == True: found = True

        # expand nodes and keep looking
        else: 
            #nodes we're testing
            possiblemoves = board._possible_moves()
            nextstates = board.next_action_states()

            #test nodes using heuristic
            minfscore = float('inf')
            length = len(nextstates)

            # print("current board: ")
            # print(board)
            bestmove = None

            for i in range(length):
                teststate = nextstates[i]
                testboard = teststate[0]
                testval = heuristic(testboard)
                #print("possible board")
                print(teststate[0])
                #print(possiblemoves)
                                
                new = newCase(closedcases, testboard)
                fscore = gscore + testval
                print("h val: " + str(testval) + " + g val: " + str(gscore) + " = fscore: " + str(fscore))
                print("will move if " + str(fscore) + " is less than " + str(minfscore) + " and newCase is true it is: " + str(new))
                
                if fscore <= minfscore and new == True:
                    print("setting good move" + str(i))
                    minfscore = fscore
                    closedcases.append(testboard)
                    bestmove = i
            

            nextmove = possiblemoves[bestmove]
            newboard = board._move(nextmove[0])
            solution.append(nextmove[1])
            limit+=1
            gscore+=1

            print("solution: "+ str(solution))
            board = newboard

            print("new board")
            print(board)

    return solution

def newCase(closedcases, board: Board):
    '''
    this tests if the board state is new or not
    '''
    length = len(closedcases)

    for i in range(length):
        if compare(board, closedcases[i]) == True:
            return False
    return True
    
def compare(self, other):
    '''
    This compares a board states to each other
    '''
    if isinstance(other, Board):
        return np.array_equal(self.state, other.state)
    return False