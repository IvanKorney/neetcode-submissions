class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def bt(sub):
            if len(sub) == n:
                res.append(sub[:])
                return
            for i in nums:
                if i in sub:
                    continue
                sub.append(i)
                bt(sub)
                sub.pop()


        bt([])



        return res