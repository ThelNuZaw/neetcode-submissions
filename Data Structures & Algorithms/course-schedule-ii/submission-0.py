class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        time = 0
        result = []
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1

        q = collections.deque()
        for n in range(numCourses):
            if(indegree[n] == 0):
                q.append(n)
        while q:
            time += 1
            n = q.popleft()
            result.append(n)
            for nei in adj[n]:
                indegree[nei] -= 1
                if(indegree[nei] == 0):
                    q.append(nei)
                
        if time != numCourses:
            return []
        return result[::-1]
