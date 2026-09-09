class Solution:
    def recurBuilder(self, n, path, final_list, num_open, num_close) -> None:

        if len(path) == n * 2:
            final_list.append("".join(path))

        if num_open < n:
            path.append('(')
            self.recurBuilder(n, path, final_list, num_open + 1, num_close)
            path.pop()
    
        if num_close < num_open:
            path.append(')')
            self.recurBuilder(n, path, final_list, num_open, num_close + 1)
            path.pop()

        return

    def generateParenthesis(self, n: int) -> List[str]:
        
        # last question for confidence booster
        path = []
        final_list = []

        num_open = 0
        num_close = 0

        self.recurBuilder(n, path, final_list, num_open, num_close)

        return final_list