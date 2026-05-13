class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        frequencyMap = [[] for i in range(len(nums) + 1)]
        obj = {}
        for i in nums:
            obj[i] = 1 + obj.get(i,0)
        for i in obj:
            frequencyMap[obj[i]].append(i) 
        for i in range(len(frequencyMap)-1,-1,-1):
            for s in frequencyMap[i]:
                res.append(s)
                k -= 1
                if k == 0:
                    return res
            
