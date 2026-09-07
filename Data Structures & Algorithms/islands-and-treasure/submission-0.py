class Solution:  
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # create a queue
        queue = deque()

        # first append all the indices with 0s
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while (queue):
            for _ in range(len(queue)):
                i, j = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

                for nr, nc in directions:
                    if i + nr >= 0 and j + nc >= 0 and i + nr < len(grid) and j + nc < len(grid[0]) and grid[i + nr][j + nc] == 2147483647:
                        grid[i + nr][j + nc] = grid[i][j] + 1
                        queue.append((i + nr, j + nc))

        return







