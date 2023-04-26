from board import Board
import numpy as np
import time
from agent import a_star_search
from agent import BF,CB, MT

def main():

    # for m in [10,20,30,40,50]:
    for m in [10,20,30,40,50]:
        cpuTime = 0
        nodes = 0
        length = 0
        found = 0
        for seed in range(0,10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)
            
            start =  time.process_time()   
            '''
            ***********************************************
            Solve the Board state here with A*
            ***********************************************
            '''
            check = a_star_search(board, CB)
            nodes += check[0]
            length += check[1]

            print("working...")
            if check[2] == True:
                found += 1

            end =  time.process_time()
            solution_cpu_time = end-start
            cpuTime += solution_cpu_time
        
        print("average time for m:" + str(m))
        print(cpuTime/10)
        print("average nodes for m:" + str(m))
        print(nodes/10)
        print("average length for m:" + str(m))
        print(length/10)
        print("success rate for m:" + str(m))
        print(found/10)

if __name__ == "__main__":
    main()