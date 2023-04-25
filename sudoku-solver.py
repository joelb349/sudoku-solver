board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 0, 0, 7, 4, 0, 0],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(board)

def find_empty(bo):
    for row, val_row in enumerate(bo):
        for col, val_col in enumerate(val_row):
            if val_col == 0:
                count += 1
                return (row, col)
    return None

empty_place = find_empty(board)
# Check ok - print(empty_place)

def fill_board(bo):
    empty = find_empty(bo)
    # While there's still zeroes in puzzle
    while empty is not None:
        row_empty, col_empty = empty
        for i in range(1, 10):
            # Put it in this spot and check it's ok.
            valid = is_digit_valid(bo, empty, i)
            if valid:
                ## Execute code here
            else:
                continue

## Note: No point doing the horizontal check if vertical comes back false
def is_digit_valid(board, empty_space, number_to_add):
    row, col = empty_space
    line = set()

    for i in range(len(board)):
        line.add(board[i][col])
    # Vertical line check
    if number_to_add not in line:
        # Horizontal logic
        line.clear()
        line.add(board[row])
        if number_to_add not in line:
            is_valid = check_mini_squares(board, number_to_add, empty_space)
            return is_valid
        else:
            return False
    else:
        return False
    
def check_mini_squares(sudoku_board, number, empty_position):
    # We can spliut this logic out dependent on where
    # empty_position 
    ## TO-DO:: Add this logic
    return None
