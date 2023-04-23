from __future__ import annotations
from board import Board
from collections.abc import Callable


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
                     [7, 8,0]])

    misplacedtiles= 0
    for row in range(3):
        for column in range(3):
            if Board[row][column] != correctboard[row][column]:
                misplacedtiles +=1
        
    return misplacedtiles


def CB(board: Board) -> int:
    '''
    For each block in the given Board get the city block distance
    and sum to the total city block distance
    '''
    totalcbd = 0

    for row in range(3):
        for column in range(3):
            tilecbd = 0

            tilecbd = getElement(Board[row][column], row, column)
            totalcbd += tilecbd
            
        
    return totalcbd

def NA(board: Board) -> int:
    #my heuristic here
    return 


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
    return
