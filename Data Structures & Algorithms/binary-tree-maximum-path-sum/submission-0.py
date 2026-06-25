# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maxleft = max(left, 0) #we never split the previous leaf nodes 
            maxright = max(right, 0)
            #split
            res[0] = max(res[0], root.val + maxleft + maxright)

            #withoutsplit
            return root.val + max(maxleft, maxright)
        dfs(root)
        return res[0]
        