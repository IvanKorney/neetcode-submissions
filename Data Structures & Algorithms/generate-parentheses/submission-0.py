class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def dfs(n,o,c):
            if o == n == c:
                return res.append("".join(sub[:]))
            else:
                if n > o:
                    sub.append('(')
                    dfs(n,o+1,c)
                    sub.pop()
                if c < o:
                    sub.append(')')
                    dfs(n,o,c+1)
                    sub.pop()
        dfs(n,0,0)
        return res