def is_row_includes(row, num, suduko):
  return suduko[row].count(num) > 1

def is_col_includes(row, col, val, suduko):
  for i in range(len(suduko)):
    if i != row and suduko[i][col] == val:
      return True
  return False

def get_start_box(row, col):
  start_col = (col // 3) * 3
  start_row = (row // 3) * 3

  return start_row, start_col

def is_in_box(row, col, val, suduko):
  start_row, start_col = get_start_box(row, col)
  
  for r in range(start_row, start_row + 3):
    for c in range(start_col, start_col + 3):
      if (r, c) != (row, col) and suduko[r][c] == val:
        return True
      
  return False

def is_valid_sudoku(sudoku):
  for row in range(9):
    for col in range(9):
      val = sudoku[row][col]
      if val == ".":
        continue

      if is_row_includes(row, val, sudoku) or \
         is_col_includes(row, col, val, sudoku) or \
         is_in_box(row, col, val, sudoku):
        return False

  return True

# Main Test-cases
board1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(board1))  # ✅ Expected: True

board2 = [
  ["5","3",".",".","7",".",".","5","."],  # two "5"s in row 0
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(board2))  # ❌ Expected: False

board3 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","6",".",".",".",".","6","."],  # two "6"s in the middle-left box
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(board3))  # ❌ Expected: False

board4 = [["."]*9 for _ in range(9)]
print(is_valid_sudoku(board4))  # ✅ Expected: True


board5 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  ["5","9","8",".",".",".",".","6","."],  # two "5"s in column 0
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(board5))  # ❌ Expected: False
