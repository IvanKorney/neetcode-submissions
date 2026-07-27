class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while True:
            cur = 0
            for i in str(n):
                cur += int(i)*int(i)
            
            if cur == 1:
                return True
            if cur in s:
                return False
            s.add(cur)
            n = cur