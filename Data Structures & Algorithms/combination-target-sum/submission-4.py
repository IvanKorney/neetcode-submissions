class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i,sub):
            if i == len(nums) or sum(sub) > target:
                return
            if sum(sub) == target:
                res.append(sub[:])
                return
            sub.append(nums[i])
            bt(i,sub)
            sub.pop()
            bt(i+1,sub)
        bt(0,[])
        return res
