<strong>GRID GENIUS:SUDOKU SOLVER</strong>
<br>
Welcome to Grid Genius, a Python-based Sudoku solver that uses backtracking to find the solution to your Sudoku puzzle.
<br>
<strong>Features</strong>
<br>
Print Sudoku Board: Visualizes the Sudoku board in a readable format.
Check Safety: Ensures the number placement follows Sudoku rules.
Solve Sudoku: Uses backtracking algorithm to solve the Sudoku puzzle.
<br>

<strong>Prerequisites</strong>
<br>
Ensure you have Python installed on your system. This code is compatible with Python 3.x.
<br>

<strong>How to Use</strong>
<br>
Clone the Repository:
<br>
git clone https://github.com/yourusername/gridsolver.git
<br>
cd gridsolver
<br>
<strong>Run the Program:</strong>
<br>
python sudoku_solver.py
<br>

<strong>Input the Sudoku Puzzle:</strong>
<br>
You will be prompted to enter the Sudoku puzzle row by row.
Use 0 to represent empty cells.
<br>

<strong>View the Solution:</strong>
<br>
The initial and solved Sudoku boards will be displayed.
<br>

<strong>Code Overview</strong>
<br>
print_board(board)
<br>
Prints the Sudoku board in a readable format, replacing 0s with .s.
<br>

is_safe(board, row, col, num)
<br>
Checks if placing a number at a given position is safe according to Sudoku rules.
<br>

solve_sudoku(board)
<br>
Uses a backtracking algorithm to solve the Sudoku puzzle. If a solution exists, it modifies the board in place.
<br>

main()
<br>
Handles user input, prints the initial board, solves the puzzle, and prints the solved board if a solution exists.
<br>

<strong> EXAMPLE </strong>
<br>
**************WELCOME TO GRID GENIUS*********************
<br>
Enter the Sudoku puzzle (use 0 for empty cells):
<br>
Enter row 1 (9 numbers separated by spaces): 5 3 0 0 7 0 0 0 0
<br>
Enter row 2 (9 numbers separated by spaces): 6 0 0 1 9 5 0 0 0
<br>
Enter row 3 (9 numbers separated by spaces): 0 9 8 0 0 0 0 6 0
<br>
Enter row 4 (9 numbers separated by spaces): 8 0 0 0 6 0 0 0 3
<br>
Enter row 5 (9 numbers separated by spaces): 4 0 0 8 0 3 0 0 1
<br>
Enter row 6 (9 numbers separated by spaces): 7 0 0 0 2 0 0 0 6
<br>
Enter row 7 (9 numbers separated by spaces): 0 6 0 0 0 0 2 8 0
<br>
Enter row 8 (9 numbers separated by spaces): 0 0 0 4 1 9 0 0 5
<br>
Enter row 9 (9 numbers separated by spaces): 0 0 0 0 8 0 0 7 9
<br>

Initial Sudoku board:
<br>
5 3 . . 7 . . . .
<br>
6 . . 1 9 5 . . .
<br>
. 9 8 . . . . 6 .
<br>
8 . . . 6 . . . 3
<br>
4 . . 8 . 3 . . 1
<br>
7 . . . 2 . . . 6
<br>
. 6 . . . . 2 8 .
<br>
. . . 4 1 9 . . 5
<br>
. . . . 8 . . 7 9
<br>

Solved Sudoku board:
<br>
5 3 4 6 7 8 9 1 2
<br>
6 7 2 1 9 5 3 4 8
<br>
1 9 8 3 4 2 5 6 7
<br>
8 5 9 7 6 1 4 2 3
<br>
4 2 6 8 5 3 7 9 1
<br>
7 1 3 9 2 4 8 5 6
<br>
9 6 1 5 3 7 2 8 4
<br>
2 8 7 4 1 9 6 3 5
<br>
3 4 5 2 8 6 1 7 9
