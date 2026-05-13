class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoMap = {}
        for i,v in enumerate(nums):
            if target-v in twoMap:
                return [twoMap[target-v],i]
            else:
                twoMap[v] = i
                
