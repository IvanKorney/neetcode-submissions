class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        n = len(nums)

        def bt():
            if len(sub) == n:
                res.append(sub[:])
                return
            for i in nums:
                if i in sub:
                    continue
                sub.append(i)
                bt()
                sub.pop()

        bt()

        return res
