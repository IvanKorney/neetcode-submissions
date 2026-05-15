class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if m < n:
            return False

        s1m, s2m = [0] * 26, [0] * 26, 

        for i in range(n):
            s1m[ord(s1[i]) - ord('a')] += 1
            s2m[ord(s2[i]) - ord('a')] += 1

        if s1m == s2m:
            return True

        for r in range(n, m):
            l = r - n
            s2m[ord(s2[r]) - ord('a')] += 1
            s2m[ord(s2[l]) - ord('a')] -= 1

            if s2m == s1m:
                return True

        return False