class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numset = set(nums)
        for i in numset:
            if i-1 not in numset:
                longest = 0
                while i+longest in numset:
                    longest += 1
                    maxLen = max(maxLen,longest)

        return maxLen
        