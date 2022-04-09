


def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[7]==mark and board[8]==mark and board[9]==mark) or
            (board[1]==mark and board[4]==mark and board[7]==mark) or
            (board[5]==mark and board[2]==mark and board[8]==mark) or
            (board[6]==mark and board[9]==mark and board[3]==mark) or
            (board[1]==mark and board[5]==mark and board[9]==mark) or
            (board[5]==mark and board[7]==mark and board[3]==mark)  )

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        else:
            return True