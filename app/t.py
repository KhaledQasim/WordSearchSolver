from __future__ import annotations
from typing import List, Dict, Optional, Tuple, Set
from enum import Enum
import sys


class Direction(Enum):
    """Enum representing possible search directions in the grid."""
    NORTH = (-1, 0)
    NORTHEAST = (-1, 1)
    EAST = (0, 1)
    SOUTHEAST = (1, 1)
    SOUTH = (1, 0)
    SOUTHWEST = (1, -1)
    WEST = (0, -1)
    NORTHWEST = (-1, -1)

    @classmethod
    def get_all_directions(cls) -> List[Direction]:
        """Get all possible search directions."""
        return list(cls.__members__.values())


class WordSearchSolver:
    """Class to solve word search puzzles in a 2D grid."""
    
    def __init__(self, grid: List[List[str]], words: List[str]) -> None:
        """
        Initialize the word search solver.
        
        Args:
            grid: 2D list of characters representing the puzzle grid
            words: List of words to find in the grid
        """
        self.grid = grid
        self.words = words
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.results: Dict[str, Optional[List[Tuple[int, int]]]] = {}
        self.found_positions: Set[Tuple[int, int]] = set()

    def solve(self) -> Dict[str, Optional[List[Tuple[int, int]]]]:
        """Solve the word search puzzle and return results."""
        for word in self.words:
            word_path = self._find_word(word)
            self.results[word] = word_path
            if word_path:
                self.found_positions.update(word_path)
        return self.results

    def get_result_grid(self) -> List[List[str]]:
        """
        Generate a visualization grid showing found words.
        
        Returns:
            2D list where:
            - Characters part of found words remain unchanged
            - Other characters are replaced with '0'
        """
        return [
            [
                cell if (row_idx, col_idx) in self.found_positions else '.'
                for col_idx, cell in enumerate(row)
            ]
            for row_idx, row in enumerate(self.grid)
        ]

    def _find_word(self, word: str) -> Optional[List[Tuple[int, int]]]:
        """Search for a single word in the grid."""
        if not word:
            return None

        first_char = word[0].upper()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col].upper() == first_char:
                    for direction in Direction.get_all_directions():
                        path = self._check_direction(word, row, col, direction)
                        if path:
                            return path
        return None

    def _check_direction(
        self,
        word: str,
        start_row: int,
        start_col: int,
        direction: Direction
    ) -> Optional[List[Tuple[int, int]]]:
        """
        Check if a word exists in a specific direction from starting position.
        
        Returns:
            List of (row, col) coordinates if found, None otherwise
        """
        path = []
        current_row, current_col = start_row, start_col
        dr, dc = direction.value

        for char in word.upper():
            if (
                current_row < 0 or current_row >= self.rows or
                current_col < 0 or current_col >= self.cols or
                self.grid[current_row][current_col].upper() != char.upper()
            ):
                return None

            path.append((current_row, current_col))
            current_row += dr
            current_col += dc

        return path


def validate_grid(grid: List[List[str]]) -> bool:
    """Validate that the grid is rectangular and non-empty."""
    if not grid or not grid[0]:
        return False
    col_count = len(grid[0])
    return all(len(row) == col_count for row in grid)


def print_grid(grid: List[List[str]]) -> None:
    """Print the grid with visual formatting."""
    border = "+" + "---+" * len(grid[0])
    print(border)
    for row in grid:
        print("| " + " | ".join(row) + " |")
        print(border)


def main() -> None:
    """Main function to demonstrate usage."""
    # Example grid and words
    
    # grid = [
    #     ['A', 'B', 'C', 'D'],
    #     ['E', 'F', 'G', 'H'],
    #     ['I', 'J', 'K', 'L'],
    #     ['M', 'N', 'O', 'P']
    # ]
    
    grid = [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'O', 'H'],
        ['I', 'J', 'W', 'L'],
        ['M', 'N', 'O', 'P']
    ]
    
    words = ['AFK', 'BGL', 'ABCD', 'MNO', 'invalid','COW']

    if not validate_grid(grid):
        print("Invalid grid format")
        sys.exit(1)

    print("Original grid:")
    print_grid(grid)

    solver = WordSearchSolver(grid, words)
    results = solver.solve()

    print("\nSearch results:")
    for word, path in results.items():
        if path:
            start = path[0]
            end = path[-1]
            print(f"Found '{word}' from {start} to {end}")
        else:
            print(f"Word '{word}' not found")

    result_grid = solver.get_result_grid()
    print("\nVisualization grid (. = unused characters):")
    print_grid(result_grid)


if __name__ == "__main__":
    main()