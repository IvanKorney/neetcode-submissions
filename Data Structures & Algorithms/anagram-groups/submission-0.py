class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}

        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in obj:
                obj[sorted_string] = []
            
            obj[sorted_string].append(s)
        
        return list(obj.values())