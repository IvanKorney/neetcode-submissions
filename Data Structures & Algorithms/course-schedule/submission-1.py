class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        dep = defaultdict(list)
    

        for course,need in pre:
            dep[course].append(need)

        vis = [0]*n

        def dfs(i):
            if vis[i] == 1:
                return True
            elif vis[i] == -1:
                return False
            
            vis[i] = 1
            for c in dep[i]:
                if dfs(c):
                    return True
                
            
            vis[i] = -1
            return False


        for i in range(n):
            if dfs(i):
                return False

        
        return True
