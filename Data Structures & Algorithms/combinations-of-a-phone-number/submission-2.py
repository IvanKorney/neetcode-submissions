class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sub = [], []
        n = len(digits)
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

        if not digits:
            return []

        def bt(index):
            if index == n:
                res.append("".join(sub[:]))
                return

            for i in numMap[digits[index]]:
                sub.append(i)
                bt(index+1)
                sub.pop()

        
        bt(0)

        return res