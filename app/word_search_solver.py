from __future__ import annotations
from typing import List, Optional, Tuple, Set, Dict
from enum import Enum
import sys


class Direction(Enum):
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
        return list(cls.__members__.values())


class WordSearchSolver:
    def __init__(self, grid: List[List[str]], words: List[str]):
        """Auto-validates and runs solver on instantiation"""
        if not self._validate_grid(grid):
            print("Invalid grid format")
            sys.exit(1)

        self.grid = grid
        self.words = words
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.results: Dict[str, Optional[List[Tuple[int, int]]]] = {}
        self.found_positions: Set[Tuple[int, int]] = set()

        self._solve()
        self._show_results()

    @staticmethod
    def _validate_grid(grid: List[List[str]]) -> bool:
        """Internal grid validation"""
        if not isinstance(grid, list) or len(grid) == 0:
            return False

        for row in grid:
            # Each row must be a list
            if not isinstance(row, list):
                return False
            # Check each element in the row is a string
            for element in row:
                if not isinstance(element, str):
                    return False

        return all(len(row) == len(grid[0]) for row in grid)

    def _solve(self) -> None:
        """Internal solve operation"""
        for word in self.words:
            path = self._find_word(word)
            self.results[word] = path
            if path:
                self.found_positions.update(path)

    def _find_word(self, word: str) -> Optional[List[Tuple[int, int]]]:
        if not word:
            return None
        first_char = word[0].upper()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col].upper() == first_char:
                    for direction in Direction.get_all_directions():
                        if path := self._check_direction(word, row, col, direction):
                            return path
        return None

    def _check_direction(self, word: str, start_row: int, start_col: int, direction: Direction) -> Optional[List[Tuple[int, int]]]:
        path = []
        current_row, current_col = start_row, start_col
        dr, dc = direction.value
        for char in word.upper():
            if not (0 <= current_row < self.rows) or \
               not (0 <= current_col < self.cols) or \
               self.grid[current_row][current_col].upper() != char.upper():
                return None
            path.append((current_row, current_col))
            current_row += dr
            current_col += dc
        return path

    def _show_results(self) -> None:
        """Auto-print results and visualization"""
        print("Search Results:")
        for word, path in self.results.items():
            if path:
                print(f"Found '{word}' from {path[0]} to {path[-1]}")
            else:
                print(f"Word '{word}' not found")

        print("\nVisualization:")
        self._print_visual_grid()

    def _print_visual_grid(self) -> None:
        """Generate and display result grid"""
        visual_grid = [
            [cell if (r, c) in self.found_positions else '.'
             for c, cell in enumerate(row)]
            for r, row in enumerate(self.grid)
        ]
        border = "+" + "---+" * self.cols
        print(border)
        for row in visual_grid:
            print("| " + " | ".join(row) + " |")
            print(border)
