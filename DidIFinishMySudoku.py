# Thanks for looking at my code. I hope you like what I have presented. I wrote it w/o any packages or many 'complex' functions in the hopes that I can convert it to C/C++
# I made it NxN scalable at the cost of readability and possibly conversion potential...

def block_check(board, N):
    block_check = True
    # avoiding 'row' and 'column' as var names because analysis would be reversed. i -> columns, j -> rows
    sqrtN = int(N**(1/2))
    for i in range(N):
        for j in range(N):
            # gentle req that number is a valid integer between 1 & N
            if board[j][i] == 0 or type(board[j][i]) != int:
                block_check = False
                return block_check
            elif 1 <= board[j][i] <= N:
                # There's only 3 rows/columns per block
                # need to remove the spillover inside the block when comparing inside the blocks
                for x in range(sqrtN):
                    for y in range(sqrtN):
                        if x == i%(sqrtN) and y == j%(sqrtN):
                            continue
                        elif board[j][i] != board[j-j%(sqrtN)+y][i-i%(sqrtN)+x]:
                            continue
                        else:
                            block_check = False
            else:
                block_check = False
                return block_check
    return block_check

def column_check(board, N):
    column_check = True
    # avoiding 'row' and 'column' as var names because analysis would be reversed. i -> columns, j -> rows
    for i in range(N):
        for j in range(N):
            # gentle req that number is a valid integer between 1 & N
            if board[j][i] == 0 or type(board[j][i]) != int:
                column_check = False
                return column_check
            elif 1 <= board[j][i] <= N:
                # if the current position is 1-N, all is fine.
                for k in range(N):
                    if k != j and board[j][i] != board[k][i]:
                        continue
                    elif k == j:
                        continue
                    else:
                        column_check = False
                        return column_check
            else:
                column_check = False
                return column_check
    return column_check

def row_checker(board, N):
    row_check = True
    # avoiding 'row' and 'column' as var names because analysis would be reversed. i -> columns, j -> rows
    for j in range(N):
        for i in range(N):
            # gentle req that number is a valid integer between 1 & N
            if board[j][i] == 0 or type(board[j][i]) != int:
                row_check = False
                return row_check
            elif 1 <= board[j][i] <= N:
                # if the current position is not 0 (is 1-N) and the current position does not equal any others in row, row is okay
                for k in range(N):
                    if k != i and board[j][i] != board[j][k]:
                        continue
                    elif k == i:
                        continue
                    else:
                        row_check = False
                        return row_check
            else:
                row_check = False
                return row_check
    return row_check

def completion_check(board):
    # This first if statement rules out erroneous entries and secures the input as the required type.
    if board and type(board) is list:
        # The first if statement is entirely in the case of a 1x1 array of value 1...
        if len(board) == 1 and type(board[0]) is int:
            if board[0] == 1:
                return True
            else:
                return False
        # This is for the remaining 99% of cases. SHOULD verify its a valid matrix size (has a sqrt). Verifies matrix dimensions are equivalent and are valid style.        
        elif len(board) >= 1 and type(board[0]) is list and len(board) == len(board[0]) and int(len(board)**(1/2))**2 == len(board):
            N = len(board)
            row_completed = row_checker(board, N)
            column_completed = column_check(board, N)
            block_completed = block_check(board, N)
            # print(row_completed, ' rows completed')
            # print(column_completed, ' columns completed')
            # print(block_completed, ' blocks completed')
            if row_completed == True and column_completed == True and block_completed == True:
                return True
            else:
                return False
        else: 
            return False    
    else:
        return False

# class Sudoku(object):
#     def __init__(self, board):
#         self.board = board
#         print(len(board))
#         print(len(board[0]))
#         print('Next Board')
# # Sudoku.self = completion_check(Sudoku)
#     def is_valid(self):
#         if completion_check(self.board) == True:
#             return True
#         else:
#             return False

def main():
    # example tests: correct 9x9 for testing
    # board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    #         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    #         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    #         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    #         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    #         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    #         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    #         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    #         ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
    # incorrect 10x9
    # board = [[1, 3, 2, 5, 7, 9, 4, 6, 8, 1]
    #         ,[4, 9, 8, 2, 6, 1, 3, 7, 5, 1]
    #         ,[7, 5, 6, 3, 8, 4, 2, 1, 9, 1]
    #         ,[6, 4, 3, 1, 5, 8, 7, 9, 2, 1]
    #         ,[5, 2, 1, 7, 9, 3, 8, 4, 6, 1]
    #         ,[9, 8, 7, 4, 2, 6, 5, 3, 1, 1]
    #         ,[2, 1, 4, 9, 3, 5, 6, 8, 7, 1]
    #         ,[3, 6, 5, 8, 1, 7, 9, 2, 4, 1]
    #         ,[8, 7, 9, 6, 4, 2, 1, 5, 3, 1]]
    # board = [] # empty board
    # board = [1] # correct board size 1
    # board = [2] # incorrect board size 1
    # board = ['a'] # incorrect str board size 1
    # board = ['incorrect str board']
    # board = [['incorrect', 'large'], ['str', 'board']]
    answer = completion_check(board)

    if answer == True:
        print("Sudoku completed!")
    elif answer == False:
        print("Sudoku board is not correctly completed! Try again.")

if __name__ == '__main__':
    main()
    # print('End of Run')