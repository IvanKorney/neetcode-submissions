class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = [0]*(len(nums)+1)
        for i,v in enumerate(nums):
            res[v] += 1
        for i in range(len(res)):
            if res[i] == 0:
                return i
