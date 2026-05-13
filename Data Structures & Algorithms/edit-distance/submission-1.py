class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(len1,len2):
            if len1 < 0:
                return len2+1
            if len2 < 0:
                return len1+1
            if (len1,len2) in memo:
                return memo[(len1,len2)]
            if word1[len1] == word2[len2]:
                return dp(len1-1,len2-1)
            insert = 1 + dp(len1,len2-1)
            delete =  1 + dp(len1-1,len2)
            replace = 1 + dp(len1-1,len2-1)
            memo[(len1,len2)] = min(insert,delete,replace)
            return memo[(len1,len2)]
        return dp(len(word1)-1,len(word2)-1)
            
            