class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        frequencyMap = [[] for i in range(len(nums) + 1)]
        obj = {}
        for n in nums:
            obj[n] = 1 + obj.get(n,0)
        for i,v in obj.items():
            frequencyMap[v].append(i)
        for arr in range(len(frequencyMap)-1,-1,-1):
            for s in frequencyMap[arr]:
                res.append(s)
                k -= 1
                if k == 0:
                    return res
