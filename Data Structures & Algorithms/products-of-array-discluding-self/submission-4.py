class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            start = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    start *= nums[j]
            res.append(start)
        return res
