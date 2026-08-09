class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q1, q2 = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                q1.append([i,c])
            else:
                q2.append([i,c])

        while q1 and q2:
            r_index, r = q1.popleft()
            d_index, d = q2.popleft()

            if r_index < d_index:
                q1.append([r_index + len(senate), r])
            else:
                q2.append([d_index + len(senate), d])
        return "Radiant" if q1 else "Dire"