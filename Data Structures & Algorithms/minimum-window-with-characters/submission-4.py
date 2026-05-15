class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        resLen = float("inf")
        window, twindow = Counter(), Counter()

        for i in t:
            twindow[i] += 1
        
        need, have = len(twindow), len(window)
        
        l,r = 0,0
        while r < len(s):
            n = s[r]
            window[n] += 1
            if window[n] == twindow[n]:
                have += 1
            while have == need:
                if resLen > r - l +1:
                    res = s[l:r+1]
                    resLen = len(res)
                m = s[l]
                window[m] -= 1
                if window[m] < twindow[m]:
                    have -= 1
                l += 1
            r += 1
        
        return res