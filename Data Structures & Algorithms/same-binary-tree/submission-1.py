# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        
        while q1 and q2:
            pcur = q1.popleft()
            qcur = q2.popleft()
            if pcur is None and qcur is None:
                continue
            if pcur is None or qcur is None or pcur.val != qcur.val:
                return False
            q1.append(pcur.left)
            q1.append(pcur.right)
            q2.append(qcur.left)
            q2.append(qcur.right)
        return True

        # if not p and not q:
        #     return True
        # if not p or not q or p.val != q.val:
        #     return False
        # return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) 
