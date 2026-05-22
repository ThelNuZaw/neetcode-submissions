# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfspostorder(root):
            nonlocal res
            if not root:
                return 0
            left = dfspostorder(root.left)
            right = dfspostorder(root.right)

            res = max(res, left + right) # diamenter of the node
            return 1 + max(left, right) # return height of current node
        
        dfspostorder(root)
        return res
