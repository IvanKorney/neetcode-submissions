class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        if c[0] > 1:
            return [0]*len(nums)

        elif c[0] == 1:
            ssum = 1
            ind = 0
            for i,v in enumerate(nums):
                if v != 0:
                    ssum *= v
                else:
                    ind = i
            res = [0]*len(nums)
            res[ind] = ssum
            return res
        ssum = 1
        for i in nums:
            ssum *= i
        res = []
        for i in nums:
            res.append(ssum//i)
        return res

        