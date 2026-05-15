class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pmap = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i in pmap:
                if not stack or stack.pop() != pmap[i]:
                    return False
            else:
                stack.append(i)






        return len(stack) == 0