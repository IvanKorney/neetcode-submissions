class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)
        for i in numset:
            if i-1 not in numset:
                longest = 0
                while i+longest in numset:
                    longest += 1
                    res = max(res,longest)
        return res
                    