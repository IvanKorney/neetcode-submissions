class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smap = {}
        l,r = 0,0
        res = 0
        while r < len(s):
            smap[s[r]] = 1 + smap.get(s[r],0)
            while smap[s[r]] > 1:
                smap[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
            r += 1
        return res