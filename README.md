ITCS 6150/8150 - Intelligent Systems
Programming Project 1 - Solving the 8-puzzle problem using A* search algorithm

# 8-Puzzle Problem Solver

This project aims to solve the 8-puzzle problem using the A* search algorithm. Two heuristics have been implemented:
- Misplaced Tiles Heuristic
- Manhattan Distance Heuristic

Programming Language: Python 3.6 or later (For installing use this link https://www.python.org/downloads/)
Compiler: MSC v.1934 64 bit (AMD64)

Submitted By: Group 13

## Files:

1. `main.py`: This is the main file that orchestrates the solving of the puzzle based on user input. It handles input validation and delegates solving to the respective heuristic module.
  
2. `misplacedTiles.py`: Implements the Misplaced Tiles Heuristic and has functionalities to solve the puzzle using this heuristic.
  
3. `manhattanDistance.py`: Implements the Manhattan Distance Heuristic and provides functionalities to solve the puzzle with it.

## How to use:

1. Run `main.py`.
   
2. You'll be prompted to select a heuristic function:
    - Input `1` for Misplaced Tiles heuristic function.
    - Input `2` for Manhattan Distance heuristic function.

3. Next, input the numbers of the 8-puzzle problem from left to right, top to bottom. The numbers should be separated by whitespace, with the empty tile represented by `0`.

4. Optionally, you can input the goal state. If you don't provide any, the default goal state [1, 2, 3, 4, 5, 6, 7, 8, 0] will be considered.

5. The program will process the input and provide a step-by-step solution if one exists.

## Validation:

The program checks for:
- Duplicate tiles.
- Number of tiles not equal to 9.
- Tile numbers less than 0 or greater than 8.

## Dependencies:
- Python Standard Library

## Notes:

- The `Node` class in both heuristic files encapsulates the details of a puzzle state, including its parent (used to backtrack solution), cost, and heuristic values.
  
- In `misplacedTiles.py`, the heuristic is the number of tiles that are not in their respective goal position.
  
- In `manhattanDistance.py`, the heuristic is the sum of Manhattan distances between each tile's current position and its goal position.
  
- The search algorithms in both heuristic files return the path to the solution, the number of nodes generated, and the number of nodes expanded.

## Troubleshooting:

If you encounter any errors or invalid inputs, the program will provide an appropriate message and prompt you to try again.