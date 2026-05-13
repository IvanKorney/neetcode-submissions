class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        sorted_s1 = "".join(sorted(s1))
        l = 0
        r = len(s1)-1
        while r < len(s2):
            sorted_s2 = "".join(sorted(s2[l:r+1]))
            if sorted_s2 == sorted_s1:
                return True
            l += 1
            r += 1
        return False





        