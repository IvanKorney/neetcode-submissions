class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i):
            if sum(sub) == target:
                return res.append(sub[:])
            elif sum(sub) > target or i >= len(nums):
                return
            else:
                sub.append(nums[i])
                dfs(i)
                sub.pop()
                dfs(i+1)
        dfs(0)
        return res
