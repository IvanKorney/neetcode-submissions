class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(c,o,sub):
            if o == c == n:
                res.append("".join(sub[:]))
                return 
            if o < n:
                sub.append("(")
                bt(c,o+1,sub)
                sub.pop()
            if c < o:
                sub.append(")")
                bt(c+1,o,sub)
                sub.pop()
        
        bt(0,0,[])
            

        return res