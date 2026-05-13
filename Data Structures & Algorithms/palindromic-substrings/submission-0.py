class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countPalindromes(i):
            count = 0
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            l, r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        for i in range(len(s)):
            res += countPalindromes(i)
        return res

        
            
