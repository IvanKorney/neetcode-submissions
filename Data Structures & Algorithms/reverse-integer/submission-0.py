class Solution:
    def reverse(self, x: int) -> int:
        res_array = []
        is_neg = False
        for i in str(x):
            if i == "-":
                is_neg = True
                continue
            else:
                res_array.append(i)
            
        res = 0
        for i in range(len(res_array)-1,-1,-1):
            res *= 10
            res += int(res_array[i])
        if is_neg:
            res *= -1
        return res if res in range(-2**31,2**31) else 0    