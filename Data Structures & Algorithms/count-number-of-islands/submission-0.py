class Solution:

    def bfs(self, grid: List[List[str]], i: int, j: int) -> None:

        if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
            return

        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.bfs(grid, i-1, j)
        self.bfs(grid, i+1, j)
        self.bfs(grid, i, j+1)
        self.bfs(grid, i, j-1)

        return 

    def numIslands(self, grid: List[List[str]]) -> int:

        numIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    numIslands += 1
                    self.bfs(grid, i, j)

        return numIslands