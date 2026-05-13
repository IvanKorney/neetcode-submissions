class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            dist = math.sqrt(x**2+y**2)
            res.append([dist,x,y])
        heapq.heapify(res)
        ress = []
        while k > 0:
            _,x,y = heapq.heappop(res)
            ress.append([x,y])
            k -= 1
        return ress

