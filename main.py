from board import Board
from agent import a_star_search
import numpy as np
import time
from agent import MT,CB,NA, BFS

'''

Hi TA if you're reading this! I didn't know how much you wanted me to change or implement
the main, but I basically have a print that gives me the nodes in agent and then I printed
the tuple with the averages here.

I just didn't know if ya'll needed to use it so I made it so it works, (with prints) and 
still runs the tests. BFS is implemented here too fyi.
'''



def main():

        for h in [MT, CB, NA, BFS]:
            for m in [10,20,30,40,50]:
                success = 0
                cputime = 0
                found = 0
                length = 0

                for seed in range(0,10):
                    # Sets the seed of the problem so all students solve the same problems

                    board = Board(m, seed)
                    
                    start =  time.process_time()   

                    '''
                    ***********************************************
                    Solve the Board state here with A*
                    ***********************************************
                    '''
                    solution = a_star_search(board,h)
                    lengthsol = len(solution)

                    
                    if board.check_solution(solution) == True:
                            found+=1

                    end =  time.process_time()
                    solution_cpu_time = end-start
                    cputime += solution_cpu_time
                    length += lengthsol

        print("(average success rate, average cpu time, average length)")
        print(((found/10), (cputime/10), length/10))
        return ((found/10), (cputime/10), length/10)



if __name__ == "__main__":
    main()
