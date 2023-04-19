from __future__ import annotations
from board import Board
from collections.abc import Callable


'''
Heuristics
'''
def MT(board: Board) -> int:
    # go through and count how many non-matches there are
    i = 1
    misplaced = 0
    for row in Board:
        for column in row:
            if i != column and column != 9:
                misplaced += 1
            i += 1;

    return misplaced

def CB(board: Board) -> int:
    #for each tile check City Block distance and sum
    return 

def NA(board: Board) -> int:
    #my heuristic here
    return 



'''
A* Search 
'''
def a_star_search(board: Board, heuristic: Callable[[Board], int]):
    return
