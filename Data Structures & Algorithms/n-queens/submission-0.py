"""
iterate through the board
for each cell we can decide: place queen or not
use backtracking for decision branching
end condition: end of the board or all n queens are placed
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        placements = []
        cells_num = n*n

        def can_place(board, position) -> bool:
            row = position // n
            column = position - (row * n)
            
            if (sum(board[row]) == 0 and sum(board[row][column] for row in range(n)) == 0):
                row_i, column_i = row, column
                while row_i < n and column_i < n:
                    if board[row_i][column_i] > 0:
                        return False
                    row_i += 1
                    column_i += 1

                row_i, column_i = row, column
                while row_i >= 0 and column_i < n:
                    if board[row_i][column_i] > 0:
                        return False
                    row_i -= 1
                    column_i += 1

                row_i, column_i = row, column
                while row_i < n and column_i >= 0:
                    if board[row_i][column_i] > 0:
                        return False
                    row_i += 1
                    column_i -= 1

                row_i, column_i = row, column
                while row_i >= 0 and column_i >= 0:
                    if board[row_i][column_i] > 0:
                        return False
                    row_i -= 1
                    column_i -= 1
                return True
            else:
                return False

        def place(board, position):
            row = position // n
            column = position - (row * n)
            board[row][column] = board[row][column] + 1

        def pick(board, position):
            row = position // n
            column = position - (row * n)
            board[row][column] = board[row][column] - 1
            
        def convert(board):
            return ["".join("Q" if cell else "." for cell in row) for row in board]
        
        def branch(board, position, queens_placed_num):
            if queens_placed_num == n:
                placements.append([row[:] for row in board])
                return
                
            if position >= cells_num:
                return

            next_position = position + 1
            branch(board, next_position, queens_placed_num)

            if can_place(board, position):
                place(board, position)
                branch(board, next_position, queens_placed_num + 1)
                pick(board, position)


        board = [[0] * n for _ in range(n)]
        branch(board, 0, 0)

        return [convert(placement) for placement in placements]

        