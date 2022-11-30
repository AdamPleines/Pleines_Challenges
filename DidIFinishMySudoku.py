# Thanks for looking at my code. I hope you like what I have presented.

def block_check(board):
    block_check = True
    # avoiding 'row' and 'column' as var names because analysis would be reversed. i -> columns, j -> rows
    for i in range(9):
        for j in range(9):
            # gentle req that number is a valid integer between 1 & 9
            if 1 <= board[j][i] <= 9 and board[j][i] == int(board[j][i]):
                # There's only 3 rows/columns per block
                # need to remove the spillover inside the block when comparing inside the blocks
                for x in range(3):
                    for y in range(3):
                        if x == i%3 and y == j%3:
                            continue
                        elif board[j][i] != board[j-j%3+y][i-i%3+x]:
                            continue
                        else:
                            block_check = False
    return block_check

def column_check(board):
    column_check = True
    # avoiding 'row' and 'column' as var names because analysis would be reversed. i -> columns, j -> rows
    for i in range(9):
        for j in range(9):
            # gentle req that number is a valid integer between 1 & 9
            if 1 <= board[j][i] <= 9 and board[j][i] == int(board[j][i]):
                # if the current position is 1-9, all is fine.
                for k in range(9):
                    if k != j and board[j][i] != board[k][i]:
                        continue
                    elif k == j:
                        continue
                    else:
                        column_check = False
    return column_check

def row_checker(board):
    row_check = True
    # avoiding 'row' and 'column' as var names because analysis would be reversed. i -> columns, j -> rows
    for j in range(9):
        for i in range(9):
            # gentle req that number is a valid integer between 1 & 9
            if 1 <= board[j][i] <= 9 and board[j][i] == int(board[j][i]):
                # if the current position is not 0 (is 1-9) and the current position does not equal any others in row, row is okay
                for k in range(9):
                    if k != i and board[j][i] != board[j][k]:
                        continue
                    elif k == i:
                        continue
                    else:
                        row_check = False
    return row_check

def completion_check(board):
    row_completed = row_checker(board)
    column_completed = column_check(board)
    block_completed = block_check(board)
    # print(row_completed, ' rows completed')
    # print(column_completed, ' columns completed')
    # print(block_completed, ' blocks completed')
    if row_completed == True and column_completed == True and block_completed == True:
        return True
    else:
        return False

def main():
    board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
            ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
            ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
            ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
            ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
            ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
            ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
            ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
            ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
    answer = completion_check(board)

    if answer == True:
        print("Sudoku completed!")
    elif answer == False:
        print("There's an error! Try again.")

if __name__ == '__main__':
    main()
    print()
    print('End of Run')