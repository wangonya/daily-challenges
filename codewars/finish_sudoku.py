from typing import List


def done_or_not(board: List[List]) -> str:
    finished = True

    for line in range(0, 9):
        def check_finished(a, b):
            if a ^ b:
                return False
            return True

        if finished is False:
            break
        row = board[line]
        column = [c[line] for c in board]
        row = set(row)
        column = set(column)
        finished = check_finished(row, column)
        if line in (0, 3, 6):
            square = []
            square_lists = board[line if line < 7 else 6:line + 3]
            for x in range(0, 7, 3):
                square.extend(square_lists[0][x:x + 3])
                square.extend(square_lists[1][x:x + 3])
                square.extend(square_lists[2][x:x + 3])
                square = set(square)
                finished = check_finished(row, square)
                finished = check_finished(column, square)
                square = []
    return 'Finished!' if finished else 'Try again!'

# def done_or_not(board):
#     for i in xrange(0, 9):
#       (l, c, b) = (set(), set(), set())
#       for j in xrange(0, 9):
#           c.add(board[i][j]) 
#           l.add(board[j][i])
#           b.add(board[0 + j / 3][((i * 3) % 9) + j % 3])
#       if len(l)!=9 or len(c)!=9 or len(b)!=9:
#           return 'Try again!'
#     return "Finished!"
