class Solution:
    def isValid(self, s: str) -> bool:
        endBracket = {"]":"[","}":"{",")":"("}
        stack = []
        for i in s:
            if i in endBracket:
                if stack and stack[-1] == endBracket[i]:
                    stack.pop()
                else: return False
            else:
                stack.append(i)

        return len(stack) == 0


        