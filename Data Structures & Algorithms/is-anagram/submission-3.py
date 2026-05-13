class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for i in s:
            smap[i] = 1 + smap.get(i,0)
        for j in t:
            tmap[j] = 1 + tmap.get(j,0)
        
        for i in smap:
            if i not in tmap or smap[i] != tmap[i]:
                return False
        return True
