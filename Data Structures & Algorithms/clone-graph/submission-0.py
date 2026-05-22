"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        Map = {}
        Map[node] = Node(node.val)
        q = collections.deque([node])

        while q:
            cur_node = q.popleft()
            for n in cur_node.neighbors:
                if n not in Map:
                    Map[n] = Node(n.val)
                    q.append(n)
                Map[cur_node].neighbors.append(Map[n])
        return Map[node]