class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        numMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrack(i, sub):
            if i == len(digits):
                res.append("".join(sub))
            else:
                for d in numMap[digits[i]]:
                    sub.append(d)
                    backtrack(i+1,sub[:])
                    sub.pop()

        backtrack(0,[])
        return res
