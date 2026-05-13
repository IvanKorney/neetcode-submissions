class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def dfs(o,c,n):
            if o == c == n:
                res.append("".join(sub))

            else:
                if o < n:
                    sub.append("(")
                    dfs(o+1,c,n)
                    sub.pop()
                if c < o:
                    sub.append(")")
                    dfs(o,c+1,n)
                    sub.pop()
        dfs(0,0,n)
        return res