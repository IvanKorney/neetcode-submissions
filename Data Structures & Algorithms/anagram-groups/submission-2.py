class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString not in obj:
                obj[sortedString] = []
            obj[sortedString].append(s)
        return list(obj.values())