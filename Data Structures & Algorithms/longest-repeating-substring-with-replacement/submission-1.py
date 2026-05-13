class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        obj = {}
        l,r = 0,0
        res = 0
        while r < len(s):
            e = s[r]
            obj[e] = 1 + obj.get(e,0)
            while r-l+1-max(obj.values()) > k:
                obj[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
            r += 1
        return res
