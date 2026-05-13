class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(sub):
            if len(sub) == len(nums):
                return res.append(sub)
            for i in nums:
                if i in sub:
                    continue
                sub.append(i)
                dfs(sub[:])
                sub.pop()
        dfs([])
        return res