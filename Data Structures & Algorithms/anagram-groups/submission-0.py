class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sobj = {}
        for i in strs:
            sorted_string = "".join(sorted(i))
            if sorted_string not in sobj:
                sobj[sorted_string] = []
            sobj[sorted_string].append(i)
        return list(sobj.values())