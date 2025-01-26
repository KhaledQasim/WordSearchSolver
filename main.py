from app import word_search_solver
from typing import List

if __name__ == '__main__':
    grid = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'O', 'H'],
        ['I', 'J', 'W', 'L'],
        ['M', 'N', 'O', 'P']
    ]

    words = ['AFK', 'BGL', 'ABCD', 'MNO', 'invalid','COW',"fwp"]
    
    word_search_solver.WordSearchSolver(grid, words)
