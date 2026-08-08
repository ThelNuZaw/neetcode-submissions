class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        #BFS
        q = deque([0])
        farthest = 0 #not to visit the same index again
        while q:
            index = q.popleft()
            start = minJump + index
            end = maxJump + index
            for i in range(max(farthest + 1, start), min(len(s), end + 1)):
                if s[i] == "0":
                    q.append(i)
                    if i == len(s) - 1:
                        return True
            farthest = index + maxJump
        return False