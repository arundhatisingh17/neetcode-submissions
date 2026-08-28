class Solution:
    def recurBoard(self, board: List[List[str]], word: str, pntr: int, i: int, j: int, visited: set) -> bool:

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[pntr] or (i, j) in visited:
            return False

        if pntr == len(word) - 1:
            return True

        visited.add((i, j))
        comb = (self.recurBoard(board, word, pntr + 1, i - 1, j, visited) or
                self.recurBoard(board, word, pntr + 1, i + 1, j, visited) or
                self.recurBoard(board, word, pntr + 1, i, j + 1, visited) or
                self.recurBoard(board, word, pntr + 1, i, j - 1, visited))

        visited.remove((i, j))

        return comb

    def exist(self, board: List[List[str]], word: str) -> bool:

        pntr = 0

        # need to maintain a visited list
        visited = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.recurBoard(board, word, pntr, i, j, visited):
                    return True

        return False
