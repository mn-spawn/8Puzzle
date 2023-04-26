from __future__ import annotations
from board import Board
from collections.abc import Callable
from queue import PriorityQueue
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
    ''' 
    Out of row and column - like simplified version of manhatten distance but also with the simplicity of
    misplaced tiles
    '''


    correctboard = ([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]])

    b = board.state

    misrow = 0
    miscol = 0

    for row in range(3):
        for column in range(3):
            if b[row][column] != correctboard[row][column]:
                correct = retCorrect(correctboard[row][column])
                if row != correct[1]:
                    misrow +=1
                if column != correct[0]:
                    miscol +=1

    return (miscol+misrow)

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

def retCorrect(num):
        '''
        Helper that returns the expected num coords
        '''
        if num == 1: return (0,1)
        elif num == 2: return (0,1)
        elif num == 3: return (0,2)
        elif num == 4: return (1,0)
        elif num == 5: return (1,1)
        elif num == 6: return (1,2)
        elif num == 7: return (2,0)
        elif num == 8: return (2,1)
        elif num == 0: return (2,2)

'''
A* Search 
'''

def a_star_search(board: Board, heuristic: Callable[[Board], int]):

    #initialize the frontier PQ and add first state
    frontier = PriorityQueue()

    #put in our fscore, tiebreak, board, and solution
    frontier.put((heuristic(board), 0, board, []))

    #will be set once we've found solution
    found = False

    #distance from start node and our entry counter (initial was 0)
    gscore = 0
    j = 1

    #what we've seen
    seenstates = {str(board): True}

    #run while the PQ is not empty
    while frontier.empty() == False or found == True:
        #pop our node
        boardtuple = frontier.get()
        testboard = boardtuple[2]

        #put it into the seenstate, shallow copy parentsolution
        seenstates[str(testboard)] = True
        parentsolution = boardtuple[3].copy()

        if testboard.goal_test() == True:
            solution = boardtuple[3]
            break

        else:
            # get children
            children = testboard.next_action_states()

            #check if we've seen
            for i in children:
                child = i[0]
                move = i[1]

                if str(child) not in seenstates:
                    #calculate
                    fscore = gscore + heuristic(child)
                    childsol = parentsolution + [move]

                    #put child into frontier
                    frontier.put((fscore, j, child, childsol))
                    j+=1

        #increase the distance from init to current node
        gscore+=1

    return solution
    