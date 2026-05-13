class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0
        for i in nset:
            if i-1 in nset:
                continue
            longest = 0
            while i+longest in nset:
                longest += 1
            res = max(res,longest)
        
        return res