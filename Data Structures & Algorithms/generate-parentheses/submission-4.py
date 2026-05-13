class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def backtrack(o,c):
            if o == c == n:
                return res.append("".join(sub[:]))
            if o < n:
                sub.append("(")
                backtrack(o+1,c)
                sub.pop()
                
            if c < o:
                sub.append(")")
                backtrack(o,c+1)
                sub.pop()
              
        backtrack(0,0)
        return res
            
        
