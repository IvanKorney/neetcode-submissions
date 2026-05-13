class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            n = str(n)
            res = 0
            for i in n:
                res += int(i)**2
            if res == 1:
                return True
            else:
                print(res,s)
                if res in s:
                    return False
                else:
                    s.add(res)
                    n = res
