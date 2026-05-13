class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums)+1)]
        obj = {}
        for s in nums:
            obj[s] = 1 + obj.get(s,0)
        for key, val in obj.items():
            freq[val].append(key)
        
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res