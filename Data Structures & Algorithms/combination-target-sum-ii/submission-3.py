class Solution:
    def combHelper(self, idx: int, candidates: List[int], target: int, path: List, final_list: List, memo: set) -> None:

        if target < 0:
            return

        if target == 0:
            final_list.append(path[::])
            return

        if idx >= len(candidates):
            return

        for i in range(idx, len(candidates)):

            if i > idx and candidates[i] == candidates[i-1]:
                continue

            path.append(candidates[i])
            self.combHelper(i + 1, candidates, target - candidates[i], path, final_list, memo)
            path.pop()

        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        path = []
        final_list = []
        memo = set()

        candidates = sorted(candidates)

        self.combHelper(0, candidates, target, path, final_list, memo)

        return final_list