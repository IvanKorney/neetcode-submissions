class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(s)
        return list(anagrams.values())