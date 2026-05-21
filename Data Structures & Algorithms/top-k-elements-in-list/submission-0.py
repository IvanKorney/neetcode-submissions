class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        c = Counter()
        freq = [[] for _ in range(n+1)]

        for i in nums:
            c[i] += 1

        for i, v in c.items():
            freq[v].append(i)

        res = []
        for i in range(n,-1,-1):
            for j in freq[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res


        return res
