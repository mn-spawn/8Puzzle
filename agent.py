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

    solution = []
    found = False 
    
    closedcases = [board]
    limit = 0
    gscore = 0
    initboard = board

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

            bestmove = None

            for i in range(length):
                teststate = nextstates[i]
                testboard = teststate[0]
                testval = heuristic(testboard)
                 
                new = newCase(closedcases, testboard)
                fscore = gscore + testval
                
                if fscore <= minfscore and new == True:
                    minfscore = fscore
                    closedcases.append(testboard)
                    bestmove = i
            

            nextmove = possiblemoves[bestmove]
            newboard = board._move(nextmove[0])
            solution.append(nextmove[1])
            limit+=1
            gscore+=1

            board = newboard

    print(solution)
    print(initboard.check_solution(solution))
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



############################## other version ######################################
    # solution = []

    # searching = True
    # limit = 0
    # gscore = 0
    
    # opencases = []
    # opencases.append(((heuristic(board)+gscore), board, 'init'))
    # print(opencases)

    # print(board)

    # closedcases = []


    # while searching and limit != 30:
    #     holdboard = opencases[0]
    #     opencases.pop(0)
    #     board = holdboard[1]

    #     if holdboard[2] != 'init':
    #         solution.append(holdboard[2])

    #     if board.goal_test() == True: 
    #         searching = False

    #     else:
    #         possiblemoves = board._possible_moves()
    #         print(possiblemoves)
    #         movestates = board.next_action_states()
    #         numofmoves = len(possiblemoves)

    #         for i in range(numofmoves):
    #             teststate = movestates[i]
    #             state = teststate[0]
                
    #             move = possiblemoves[i]
    #             movestring = move[1]

    #             new = newCase(closedcases, state)

    #             if new == True:
    #                 opencases.append(((heuristic(state)+gscore), state, movestring))


    #         closedcases.append(board)
    #         opencases.sort(key=lambda a: a[0])

    #         gscore += 1
    #         limit += 1

    # print(solution)
    # return solution