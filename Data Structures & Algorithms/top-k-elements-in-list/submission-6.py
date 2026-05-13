class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for _ in range(len(nums)+1)]
        obj = {}
        for i in nums:
            obj[i] = 1 + obj.get(i,0)
        
        for i, v in obj.items():
            freq[v].append(i)

        for i in range(len(freq)-1,-1,-1):
            if freq[i]:
                for e in freq[i]:
                    res.append(e)
                    k -= 1
                    if k == 0:
                        return res
        
        return res



