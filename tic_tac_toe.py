#The challenge was to devise a representation of an NxN tic-tac-toe game board, 
#such that a win can be verified in O(1) time.

def play_game(board_size):
    board = init_board(board_size)
    win_matrix = init_win_matrix(board_size)
    player_turn = 1
    winner = False
    num_moves = 0
    max_num_moves = board_size ** 2

    print_board(board)

    while winner == False and num_moves < max_num_moves:
        x,y = get_move(player_turn)
        place_move(x,y,board, player_turn)
        winner = record_coord(x,y,win_matrix, player_turn, board_size, 3)
        print_board(board)
        player_turn *= -1
        num_moves += 1

    if winner == False:
        return "tie"
    else:
        return "player " + str(winner) + " wins"

def parse_raw_input(user_input):
    user_input = user_input.split(',')
    parsed_input = [int(i) for i in user_input]
    return parsed_input

def get_move(player_turn):
    print "player " + str(player_turn) + "'s move"
    user_input = raw_input()
    user_input_parsed = parse_raw_input(user_input)
    return user_input_parsed

def place_move(x , y,board, player_turn):
    board[y][x] = player_turn

def print_board(board):
    for row in board:
        print row

def record_coord(x, y, win_matrix, player_side, board_size, win_num):
    row_idx = 0
    col_idx = 1
    diag_idx = 2
    bl_tr_idx = 0
    tl_br_idx = 1

    win_matrix[row_idx][y] += player_side
    win_matrix[col_idx][x] += player_side
    if x == y:
        win_matrix[diag_idx][tl_br_idx] += player_side
    if board_size - x == y:
        win_matrix[diag_idx][bl_tr_idx] += player_side

    if win_matrix[row_idx][y] == win_num or win_matrix[col_idx][x] == win_num or win_matrix[diag_idx][tl_br_idx] == win_num or win_matrix[diag_idx][bl_tr_idx] == win_num:
        return 1
    elif win_matrix[row_idx][y] == -win_num or win_matrix[col_idx][x] == -win_num or win_matrix[diag_idx][tl_br_idx] == -win_num or win_matrix[diag_idx][bl_tr_idx] == -win_num:
        return -1

    return False

def init_board(board_size):
    board = [[0 for i in range(board_size)] for i in range(board_size)]
    return board

def init_win_matrix(board_size):
    win_matrix = [[0 for i in range(board_size)],
                  [0 for i in range(board_size)],
                  [0,0]]
    return win_matrix

print play_game(3)