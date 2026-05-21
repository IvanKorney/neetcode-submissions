class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}

        for i,v in enumerate(nums):
            if target-v in obj:
                return [obj[target-v],i]
            obj[v] = i
