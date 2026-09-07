class Solution:
    def dfs(self, board: List[List[str]], i: int, j: int) -> None:

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == 'A' or board[i][j] == 'X':
            return

        if board[i][j] == 'O':
            board[i][j] = 'A'

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)

        return

    def solve(self, board: List[List[str]]) -> None:
        
        # need to capture regions that are surrounded

        # run a dfs loop to exlude all the Os that are not boundary
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        self.dfs(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'A':
                    board[i][j] = 'O'

        return
