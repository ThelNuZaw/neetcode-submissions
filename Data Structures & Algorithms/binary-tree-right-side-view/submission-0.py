# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque([root])
        res = []
        while q:
            right = None
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                if node:
                    right = node
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
            if right:
                res.append(right.val)
        return res
