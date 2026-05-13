class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = defaultdict(set)
        for i in nums:
            counter[i] = 1
        for i in range(len(nums)+1):
            if not counter[i]:
                return i
