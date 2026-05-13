class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def bt():
            if len(sub) == len(nums):
                return res.append(sub[:])
            else:
                for i in nums:
                    if i in sub:
                        continue
                    sub.append(i)
                    bt()
                    sub.pop()
        bt()
        return res