class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        resLen = float('inf')
        tmap = {}
        for i in t:
            tmap[i] = 1 + tmap.get(i,0)
        window = {}
        need = len(tmap)
        have = 0
        r,l = 0,0
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have += 1
            while need == have:
                if(r-l+1 < resLen):
                    resLen = r-l+1
                    res = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in tmap and tmap[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
            r += 1
            
        return res
