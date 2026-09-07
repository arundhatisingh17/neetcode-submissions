class Solution:
    def dfs(self, grid: List[List[int]], i: int, j: int, area: int) -> int:

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0

        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        area = 1
        area += self.dfs(grid, i + 1, j, area)
        area += self.dfs(grid, i - 1, j, area)
        area += self.dfs(grid, i, j + 1, area)
        area += self.dfs(grid, i, j - 1, area)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # last question, then chill
        maxArea = 0
        area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, area)
                    maxArea = max(maxArea, area)

        return maxArea
