class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        numMap = [[] for i in range(len(nums)+1)]
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        for i, v in freq.items():
            numMap[v].append(i)
        for index in range(len(numMap)-1,-1,-1):
            for num in numMap[index]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res