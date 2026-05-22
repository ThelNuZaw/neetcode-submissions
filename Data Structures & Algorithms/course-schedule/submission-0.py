class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #set up the adjacent list
        indegree = [0] * numCourses #[0,0,0,...n-1] for pre course
        adj = [[] for _ in range(numCourses)] #[[],[], ...]
        for crs, pre in prerequisites:
            adj[crs].append(pre) # if [1,0], 1->0 [[],[0]]
            indegree[pre] += 1 # count the inward degree of a node [1,...]
        time = 0
        q = deque()
        for i in range(numCourses):
            if(indegree[i] == 0):
                q.append(i)
        while q:
            n = q.popleft();
            time += 1
            for neighbors in adj[n]:
                indegree[neighbors] -= 1
                if (indegree[neighbors] == 0):
                    q.append(neighbors)

        return time == numCourses
            


        