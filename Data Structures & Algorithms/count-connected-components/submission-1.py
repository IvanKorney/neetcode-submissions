class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dep = defaultdict(list)

        for a, b in edges:
            dep[a].append(b)
            dep[b].append(a)

        res = 0 
        vis = set()

        def bfs(i):
            if i in vis:
                return

            vis.add(i)
            for b in dep[i]:
                bfs(b)
            


        for i in range(n):
            if i not in vis:
                res += 1
                bfs(i)

        return res