class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = {}
        for i, v in enumerate(nums):
            if target-v in resMap:
                return [resMap[target-v],i]
            else:
                resMap[v] = i
