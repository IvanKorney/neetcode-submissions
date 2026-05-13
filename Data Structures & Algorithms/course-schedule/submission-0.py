class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        dep = defaultdict(list)
        for i,j in prerequisites:
            dep[i].append(j)
            
        visit = [0]*n

        def dfs(node):
            if visit[node] == 1:
                return True
            if visit[node] == -1:
                return False
            visit[node] = 1
            for p in dep[node]:
                if dfs(p):
                    return True
            visit[node] = -1
            return False 
        for i in range(n):
            if dfs(i):
                return False
        return True