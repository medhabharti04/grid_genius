def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_safe(board, row, col, num):
    """Check if it's safe to place the number in the given position."""
    # Check the row
    if num in board[row]:
        return False
   
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
   
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
   
    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    """Main function to handle input and solve the Sudoku puzzle."""
    print("")
    print("")
    print("**************WELCOME TO GRID GENIUS*********************")
    print("Enter the Sudoku puzzle (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1} (9 numbers separated by spaces): ").strip().split()))
                if len(row) != 9:
                    raise ValueError("Each row must contain exactly 9 numbers.")
                board.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter 9 integers separated by spaces.")
   
    print("\nInitial Sudoku board:")
    print_board(board)
   
    if solve_sudoku(board):
        print("\nSolved Sudoku board:")
        print_board(board)
    else:
        print("No solution exists for the Sudoku puzzle.")

if __name__ == "__main__":
    main()

