class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[','}':'{',')':'('}
        stack = []
        for i in s:
            if i in brackets:
                if not stack or stack[-1] != brackets[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0