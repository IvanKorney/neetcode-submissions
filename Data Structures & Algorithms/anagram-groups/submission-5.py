class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in res:
                res[sorted_string] = []
            res[sorted_string].append(s)
        return list(res.values())