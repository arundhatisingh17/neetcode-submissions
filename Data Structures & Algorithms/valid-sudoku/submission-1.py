class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # iterate through each of the rows of sudoku one-by-one
        for i in range(len(board)):
            row_set = set()
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])

        # iterate through each of the columns of the sudoku one-by-one
        for i in range(len(board[0])):
            col_set = set()
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])

        for i in range(3):
            for j in range(3):

                box_set = set()

                start_row = i * 3
                start_col = j * 3

                for k in range(start_row, start_row + 3):
                    for l in range(start_col, start_col + 3):
                        if board[k][l] != "." and board[k][l] in box_set:
                            return False
                        box_set.add(board[k][l])

        return True