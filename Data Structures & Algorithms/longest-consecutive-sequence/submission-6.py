class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0
        for i in nset:
            if i-1 not in nset:
                longest = 0
                while i + longest in nset:
                    longest += 1
                res = max(longest,res)
        return res