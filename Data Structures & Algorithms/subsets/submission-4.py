class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def sub(i,s):
            if i == n:
                res.append(s[:])
                return
            
            s.append(nums[i])
            sub(i+1,s)
            s.pop()
            sub(i+1,s)
            return

        
        sub(0,[])


        return res