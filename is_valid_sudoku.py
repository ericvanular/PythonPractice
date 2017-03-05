#determine whether a given sudoku puzzle is valid

def check_valid_group(group):
    sorted_group = sorted(group)

    # print group

    for x in range(9):
        if sorted_group[x] > 9 or sorted_group[x] < 1:
            return False

    for x in range(1, 9):
        if x != 0:
            if sorted_group[x] == sorted_group[x - 1]:
                return False

    return True

def create_col(board, idx):
    col = []
    for y in range(9):
        col.append(board[y][idx])

    return col

def create_box(board, idx):
    #box 0 -> top left
    #box 1 -> top middle
    #box 8 -> bottom right
    box = []

    y_offset = (idx // 3) * 3
    x_offset = (idx % 3) * 3



    for y in range(3):
        for x in range(3):
            box.append(board[y + y_offset][x + x_offset])
    return box

def sudoku_checker(board):
    for i in range(9):
        row = board[i]
        col = create_col(board, i)
        box = create_box(board, i)

        #for debugging only
        if check_valid_group(row) is False:
            print "False at row " + str(row)
        if check_valid_group(col) is False:
            print "False at col " + str(col)
        if check_valid_group(box) is False:
            print "False at box " + str(box)
        #actual return statement
        if check_valid_group(row) is False or check_valid_group(col) is False or check_valid_group(box) is False:
            return False


    return True

def create_board(board_str):
    board = []

    for line in board_str.split("\n"):
        line = line.split()
        board.append([int(i) for i in line])

    return board

sudoku = '''3 4 5 6 7 8 9 1 2
6 7 8 9 1 2 3 4 5
9 1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 3 4 5 6 7 8 9 1
5 6 7 8 9 1 2 3 4
8 9 1 2 3 4 5 6 7'''

board = create_board(sudoku)
#print board
print "\n\n"
print sudoku_checker(board)