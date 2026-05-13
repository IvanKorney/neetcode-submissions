class Solution:
    def isValid(self, s: str) -> bool:
        closed = {')':"(",'}':"{",']':"["}
        stack = []
        for i in s:
            if i in closed:
                if stack and stack[-1]==closed[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False