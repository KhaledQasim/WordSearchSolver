from app import word_search_solver


if __name__ == '__main__':
    grid1 = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'O', 'H'],
        ['I', 'J', 'W', 'L'],
        ['M', 'N', 'O', 'P']
    ]
    grid2 = [
        ['L', 'S', 'P', 'O', 'L', 'L', 'E', 'N', 'Z', 'C', 'S', 'X'],
        ['E', 'T', 'E', 'I', 'K', 'I', 'F', 'L', 'O', 'W', 'E', 'R'],
        ['A', 'E', 'T', 'G', 'I', 'N', 'G', 'Y', 'A', 'M', 'I', 'L'],
        ['V', 'M', 'A', 'I', 'S', 'F', 'R', 'O', 'N', 'P', 'L', 'S'],
        ['E', 'M', 'L', 'O', 'K', 'R', 'O', 'Q', 'C', 'L', 'D', 'E'],
        ['S', 'O', 'I', 'L', 'I', 'N', 'O', 'N', 'I', 'A', 'I', 'E'],
        ['D', 'N', 'S', 'H', 'O', 'O', 'T', 'S', 'N', 'N', 'N', 'D'],
        ['E', 'G', 'L', 'O', 'N', 'L', 'S', 'O', 'G', 'T', 'G', 'N'],
        ['W', 'A', 'T', 'E', 'R', 'C', 'Y', 'C', 'L', 'I', 'F', 'E']
    ]
    grid3 = [
    ['t', 'u', 'd', 'e', 'p', 'u', 's', 'i', 'u', 'i', 'v', 'w', 'd', 's', 'x', 'g', 'i', 'g', 'e', 'q', 'm'],
    ['e', 'a', 'i', 'm', 'm', 'a', 't', 'u', 'r', 'e', 'v', 'r', 'm', 'u', 'n', 'a', 'm', 'q', 'p', 'a', 'o'],
    ['v', 's', 'm', 'o', 'o', 'k', 'e', 'a', 'd', 'u', 'v', 'e', 'c', 'b', 'd', 'r', 'm', 'b', 'u', 'f', 'x'],
    ['g', 'n', 'p', 'r', 'i', 'l', 'q', 'f', 'e', 'm', 'e', 'a', 't', 't', 'w', 'd', 'o', 'h', 'n', 'i', 's'],
    ['n', 'm', 'o', 'g', 's', 'n', 'j', 'p', 'e', 'r', 'c', 't', 'o', 'o', 'a', 'e', 'r', 'u', 'i', 'm', 'e'],
    ['i', 's', 's', 'o', 's', 'd', 'e', 'n', 't', 'r', 't', 'n', 'i', 't', 'c', 'n', 't', 'i', 's', 'm', 'n'],
    ['n', 'u', 's', 't', 'i', 'n', 'c', 'h', 'a', 'n', 'r', 'e', 'u', 'a', 'o', 'i', 'a', 'k', 'h', 'o', 'd'],
    ['n', 'b', 'i', 't', 'm', 'e', 'm', 'p', 'e', 'a', 'm', 'e', 'i', 'l', 'e', 'n', 'l', 'j', 'm', 'b', 'e'],
    ['i', 'h', 'b', 'e', 'r', 's', 'e', 'i', 'n', 'r', 'e', 's', 'd', 'l', 'n', 'g', 'i', 'x', 'e', 'i', 't'],
    ['g', 'e', 'l', 'n', 'e', 's', 'n', 'l', 'c', 'u', 'p', 'x', 's', 'i', 'e', 'a', 'u', 'c', 'n', 'l', 'i'],
    ['e', 'a', 'e', 's', 't', 't', 't', 'i', 'm', 'm', 'e', 'd', 'i', 'a', 't', 'e', 'h', 'v', 't', 'e', 'l'],
    ['b', 'd', 'w', 'i', 'n', 'n', 'n', 'n', 'm', 'e', 'e', 'i', 'c', 'g', 'u', 'g', 'n', 'a', 'e', 'i', 'o'],
    ['h', 'i', 'v', 'a', 'i', 'n', 'x', 'e', 'p', 'u', 'f', 'i', 's', 'h', 'r', 'n', 'e', 't', 'm', 's', 'p'],
    ['u', 'n', 'a', 'v', 'i', 'm', 'p', 'o', 'r', 't', 'a', 'n', 't', 'e', 'r', 't', 'g', 'h', 'e', 'e', 'm'],
    ['k', 'g', 'm', 'b', 'e', 'g', 'i', 'n', 't', 'e', 'r', 'c', 'e', 'p', 't', 'p', 'e', 'r', 'n', 'v', 'i'],
    ['f', 'r', 'e', 'i', 'm', 'p', 'e', 'r', 'f', 'e', 'c', 't', 'l', 'f', 'g', 'm', 'r', 'n', 'y', 'a', 'o'],
    ['o', 'd', 'e', 't', 'i', 'm', 'i', 'l', 'm', 't', 'n', 'e', 'i', 't', 'a', 'p', 'm', 'i', 'b', 'u', 's']
    ]

    words1 = ['ABC', 'OJE', 'DHL', 'INVALID']
    words2 = ['FLOWER', 'SOIL', 'WATER', 'SHOOT', 'POLLEN', "INVALID","tea","ROOT"]
    words3 = ['impossible', 'immature', 'imperfect', 'important', 'immediate', 'immobile', "immortal","impolite","improper","impatient"]
  
    word_search_solver.WordSearchSolver(grid1, words1)
 
