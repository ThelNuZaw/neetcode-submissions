# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        res = []
        
        q.append(root)
        level = 0
        while q:
            len_q = len(q)
            res.append([])
            for i in range(len_q):
                
                node = q.pop(0)
                res[level].append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            level += 1
        return res

        