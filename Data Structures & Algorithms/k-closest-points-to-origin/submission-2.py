class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        subs = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            subs.append([dist,x,y])
        heapq.heapify(subs)
        for i in range(len(subs)):
            [dist, x ,y] = heapq.heappop(subs)
            res.append([x,y])
            k -= 1
            if k == 0:
                return res
        return res