class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []
        def dfs(i):
            if sum(sub) == target:
                return res.append(sub[:])
            elif i >= len(candidates) or sum(sub) > target:
                return
            else:
                sub.append(candidates[i])
                dfs(i+1)
                sub.pop()
                while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                    i += 1
                dfs(i+1)
        dfs(0)
        return res