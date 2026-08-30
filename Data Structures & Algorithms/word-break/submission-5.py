class Solution:

    def recurBuilder(self, s: str, wordDict: set(wordDict), i: int, memo: dict) -> bool:

        if i == len(s):
            return True

        if i in memo:
            return memo[i]

        for j in range(i, len(s)):
            if s[i : j + 1] in wordDict and self.recurBuilder(s, wordDict, j + 1, memo):
                memo[i] = True
                return True

        memo[i] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.recurBuilder(s, set(wordDict), 0, memo)
        