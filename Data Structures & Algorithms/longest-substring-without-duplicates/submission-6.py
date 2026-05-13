class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        obj = {}
        res = 0
        l,r = 0,0
        while r < len(s):
            e = s[r]
            obj[e] = 1 + obj.get(e,0)
            while obj[e] == 2:
                obj[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
            r += 1
        return res