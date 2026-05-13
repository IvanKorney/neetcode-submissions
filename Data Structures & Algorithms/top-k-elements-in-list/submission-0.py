class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        arr = [[] for i in range(len(nums)+1)]
        table = {}
        for i in nums:
            table[i] = 1 + table.get(i,0)
        for key,value in table.items():
            arr[value].append(key)
        
        for i in range(len(arr)-1,-1,-1):
            for num in arr[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res

