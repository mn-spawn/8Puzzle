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

    '''
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

    searching = True
    limit = 0
    gscore = 0
    
    opencases = []
    closedcases = []

    print((heuristic(board)+gscore))
    opencases.append(((heuristic(board)+gscore), board))

    print("start board: ")
    print(board)

    while searching and limit != 30:
        holdboard = opencases[0]
        board = holdboard[1]
        print(board)

        if board.goal_test() == True: 
            searching = False
            print("solved")
        
        else:
            possiblemoves = board._possible_moves()
            movestates = board.next_action_states()
            numofmoves = len(possiblemoves)

            for i in range(numofmoves):
                teststate = movestates[i]
                state = teststate[0]
                if newCase(closedcases, state) == True:
                    opencases.append(((heuristic(state)+gscore), state))

            closedcases.append(board)
            opencases.sort(key=lambda a: a[0])

            # print(closedcases)
            # print(opencases)
            gscore += 1
            limit += 1

    return solution



'''
Down here are helper functions
'''
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
