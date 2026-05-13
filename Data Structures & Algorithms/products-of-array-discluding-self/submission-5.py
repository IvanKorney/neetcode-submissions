class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_no_zero = 1
        zeroCount = 0
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                product_no_zero *= n
            if zeroCount > 1:
                product_no_zero = 0
            product*= n
        res = []
        for i in nums:
            if i == 0:
                res.append(product_no_zero)
            else:
                res.append(int(product/i))
        return res
