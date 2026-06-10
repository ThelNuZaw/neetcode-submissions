"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deepcopy = {None:None}
        cur = head
        #copy the nodes(val = #, next = None, random = None)
        while cur:
            deepcopy[cur] = Node(cur.val) # {A = A'}
            cur = cur.next

        #set the pointers
        cur = head
        while cur:
            copy = deepcopy[cur]
            copy.next = deepcopy[cur.next]
            copy.random = deepcopy[cur.random]
            cur = cur.next
        return deepcopy[head]