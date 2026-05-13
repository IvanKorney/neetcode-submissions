class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        res = 0

        for i in n:
            if i - 1 not in n:
                longest = 0
                while i+ longest in n:
                    longest += 1
                res = max(res,longest)

        return res