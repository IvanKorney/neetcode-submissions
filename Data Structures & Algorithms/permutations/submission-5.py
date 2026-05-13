class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(sub):
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            else:
                for i in nums:
                    if i in sub:
                        continue
                    sub.append(i)
                    bt(sub)
                    sub.pop()
        bt([])
        return res
