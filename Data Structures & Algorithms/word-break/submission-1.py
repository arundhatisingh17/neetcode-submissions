class Solution:
    def recurBuilder(self, s: str, wordDict: set, i: int, memo: dict) -> bool:

        if i == len(s):
            return True

        if i in memo:
            return memo[i]

        for j in range(i + 1, len(s) + 1):
            if s[i : j] in wordDict and self.recurBuilder(s, wordDict, j, memo):
                memo[i] = True
                return True

        memo[i] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.recurBuilder(s, set(wordDict), 0, memo)