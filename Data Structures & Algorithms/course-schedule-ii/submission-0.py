class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        dep = defaultdict(list)

        for course, need in pre:
            dep[course].append(need)

        vis = [0]*n
        res = []

        def dfs(i):
            if vis[i] == 1:
                return True
            elif vis[i] == -1:
                return False
            
            vis[i] = 1
            for course in dep[i]:
                if dfs(course):
                    return True

            res.append(i)

            vis[i] = -1
            return False

        for i in range(n):
            if dfs(i):
                return []

        return res






