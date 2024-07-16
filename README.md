<strong>GRID GENIUS:SUDOKU SOLVER</strong>
Welcome to Grid Genius, a Python-based Sudoku solver that uses backtracking to find the solution to your Sudoku puzzle.

<strong>Features</strong>
Print Sudoku Board: Visualizes the Sudoku board in a readable format.
Check Safety: Ensures the number placement follows Sudoku rules.
Solve Sudoku: Uses backtracking algorithm to solve the Sudoku puzzle.
<br>

<strong>Prerequisites</strong>
Ensure you have Python installed on your system. This code is compatible with Python 3.x.

<strong>How to Use</strong>
Clone the Repository:

git clone https://github.com/yourusername/gridsolver.git
cd gridsolver

<strong>Run the Program:</strong>
python sudoku_solver.py

<strong>Input the Sudoku Puzzle:</strong>
You will be prompted to enter the Sudoku puzzle row by row.
Use 0 to represent empty cells.

<strong>View the Solution:</strong>
The initial and solved Sudoku boards will be displayed.

<strong>Code Overview</strong>
print_board(board)
Prints the Sudoku board in a readable format, replacing 0s with .s.

is_safe(board, row, col, num)
Checks if placing a number at a given position is safe according to Sudoku rules.

solve_sudoku(board)
Uses a backtracking algorithm to solve the Sudoku puzzle. If a solution exists, it modifies the board in place.

main()
Handles user input, prints the initial board, solves the puzzle, and prints the solved board if a solution exists.

<strong> EXAMPLE </strong>
**************WELCOME TO GRID GENIUS*********************
Enter the Sudoku puzzle (use 0 for empty cells):
Enter row 1 (9 numbers separated by spaces): 5 3 0 0 7 0 0 0 0
Enter row 2 (9 numbers separated by spaces): 6 0 0 1 9 5 0 0 0
Enter row 3 (9 numbers separated by spaces): 0 9 8 0 0 0 0 6 0
Enter row 4 (9 numbers separated by spaces): 8 0 0 0 6 0 0 0 3
Enter row 5 (9 numbers separated by spaces): 4 0 0 8 0 3 0 0 1
Enter row 6 (9 numbers separated by spaces): 7 0 0 0 2 0 0 0 6
Enter row 7 (9 numbers separated by spaces): 0 6 0 0 0 0 2 8 0
Enter row 8 (9 numbers separated by spaces): 0 0 0 4 1 9 0 0 5
Enter row 9 (9 numbers separated by spaces): 0 0 0 0 8 0 0 7 9

Initial Sudoku board:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Solved Sudoku board:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
