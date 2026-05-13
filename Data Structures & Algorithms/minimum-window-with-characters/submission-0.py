class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        l,r = 0, 0
        smap = {}
        resLen = float('inf')
        res = ''
        for i in t:
            smap[i] = 1 + smap.get(i,0)
        have,need = 0, len(smap)
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in smap and smap[s[r]]==window[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in smap and smap[s[l]] != window[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return res
