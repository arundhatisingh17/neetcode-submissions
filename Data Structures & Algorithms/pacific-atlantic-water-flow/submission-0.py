class Solution:

    def dfs(self, heights: List[List[int]], i: int, j: int, ans_set: set, boundary_val: int):

        if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] < boundary_val:
            return

        if (i, j) in ans_set:
            return

        if heights[i][j] >= boundary_val:
            ans_set.add((i, j))

        self.dfs(heights, i + 1, j, ans_set, heights[i][j])
        self.dfs(heights, i, j + 1, ans_set, heights[i][j])
        self.dfs(heights, i - 1, j, ans_set, heights[i][j])
        self.dfs(heights, i, j - 1, ans_set, heights[i][j])
        
        return

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_list = set()
        atlantic_list = set()
        
        # last question, then we make cool coffee!
        # for Pacific
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    boundary_val = heights[i][j]
                    self.dfs(heights, i, j, pacific_list, boundary_val)

        # for Atlantic
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    boundary_val = heights[i][j]
                    self.dfs(heights, i, j, atlantic_list, boundary_val)

        return list(pacific_list.intersection(atlantic_list))


        