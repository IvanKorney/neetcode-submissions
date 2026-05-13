class Solution:
    def isValid(self, s: str) -> bool:
        endBracket = {"]":"[","}":"{",")":"("}
        stack = []
        for d in s:
            if d in endBracket:
                if stack and stack[-1] == endBracket[d]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(d)
        return len(stack) == 0


        