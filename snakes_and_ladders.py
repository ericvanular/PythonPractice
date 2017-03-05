#determine the min number of moves to finish a game of snakes and ladders
#https://www.hackerrank.com/challenges/the-quickest-way-up

def init_board(snakes, ladders):
    board = [i for i in range(100)]

    for snake_start, snake_end in snakes:
        board[snake_start - 1] = snake_end - 1
            
    for ladder_start, ladder_end in ladders:
        board[ladder_start - 1] = ladder_end - 1
    
    
    return board



def init_num_moves(board):
    num_moves = [None for i in range(100)]
    
    for x in range(6):
        if board[x] > x:
            num_moves[board[x]] = 1
            #print "ladder from " + str(x) + " to " + str(board[x])
        num_moves[x] = 1
        if board[x] < x:
            num_moves[x] = 's'
                  
        
    prev_squares = num_moves[:6]
    
    for x in range(6, 100):
        num_moves_possible = 1 + min(prev_squares)
        if num_moves[x] is None or num_moves_possible < num_moves[x]:
            num_moves[x] = num_moves_possible
        if board[x] > x:
            #print "ladder from " + str(x) + " to " + str(board[x]) + " with move val " + str(num_moves_possible)
            num_moves[board[x]] = num_moves_possible
        elif board[x] < x:
            num_moves[x] = 'x'
            #print "snake from " + str(x) + " to " + str(board[x]) + " with move val " + str(num_moves_possible)
        if x != 99:
            prev_squares.pop(0)
            prev_squares.append(num_moves[x])
        
    return num_moves
        
    
        
    


board = '''2
3
32 62
42 68
12 98
7
95 13
97 25
93 37
79 27
75 19
49 47
67 17
4
8 52
6 80
26 42
2 72
9
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21'''

board = board.split("\n")

#ladders_flag = False
puzzle_num = 0
num_1_width_lines = 0


snakes = []
ladders = []
for idx, line in enumerate(board):
    if idx != 0:
        if len(line) == 1:
            num_1_width_lines += 1
            #print "got here"
            if num_1_width_lines % 2 == 1:
                num_ladders = int(line)
                ladders_flag = True
                
                if num_1_width_lines >= 3:
                    #print ladders
                    board =  init_board(snakes, ladders)
                    print board
                    print "\n\n"
                    num_moves = init_num_moves(board)
                    print num_moves
                    #print ladders
                    #print snakes
                ladders = []
                
            else:
                num_ladders = int(line)
                ladders_flag = False
                snakes = []
        else:
            line = [int(i) for i in line.split()]
            if ladders_flag == True:
                ladders.append(line)
            else:
                snakes.append(line)
        

print "\n\n"

board =  init_board(snakes, ladders)
print board
print "\n\n"
num_moves = init_num_moves(board)
print num_moves
