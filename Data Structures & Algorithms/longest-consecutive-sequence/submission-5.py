class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for s in numset:
            if s-1 not in numset:
                longest = 0
                while s+longest in numset:
                    longest += 1
                    res = max(res,longest)
        return res