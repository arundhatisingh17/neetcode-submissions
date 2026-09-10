class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

    def recurBuilder(self, path: List, final_list: List, start: int, s: str) -> None:

        if start == len(s):
            final_list.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            if self.isPalindrome(s[start : end]):
                path.append(s[start : end])
                self.recurBuilder(path, final_list, end, s)
                path.pop()

        return

    def partition(self, s: str) -> List[List[str]]:
        
        final_list = []
        path = []

        self.recurBuilder(path, final_list, 0, s)

        return final_list