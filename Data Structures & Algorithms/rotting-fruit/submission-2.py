class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # get this right at the first shot!
        queue = deque()
        num_minutes = 0

        num_fresh_fruits = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    num_fresh_fruits += 1

        if num_fresh_fruits == 0:
            return 0

        while (queue):
            if num_fresh_fruits == 0:
                return num_minutes
            num_minutes += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for nr, nc in directions:
                    if i + nr >= 0 and j + nc >= 0 and i + nr < len(grid) and j + nc < len(grid[0]) and grid[i + nr][j + nc] == 1:
                        num_fresh_fruits -= 1
                        grid[i + nr][j + nc] = 2
                        queue.append((i + nr, j + nc)) 

        if num_fresh_fruits != 0:
            return -1

        return num_minutes