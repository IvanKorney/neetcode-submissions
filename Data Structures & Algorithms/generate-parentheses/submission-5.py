class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []
        def bt(o,c):
            if o == n and c == n:
                return res.append("".join(sub[:]))
            if o < n:
                sub.append("(")
                bt(o+1,c)
                sub.pop()
            if c < o:
                sub.append(")")
                bt(o,c+1)
                sub.pop()

        bt(0,0)
        return res


