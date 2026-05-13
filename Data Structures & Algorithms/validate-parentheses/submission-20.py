class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[','}':'{',')':'('}
        stack = []
        for b in s:
            if b in brackets:
                if not stack or stack[-1] != brackets[b]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(b)
        return len(stack) == 0