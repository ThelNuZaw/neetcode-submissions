# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        node = TreeNode(val)
        if not root:
            return node
        while cur:
            if cur.val < val and cur.right is not None:
                cur = cur.right
            elif cur.val > val and cur.left is not None:
                cur = cur.left
            else:
                break
            
        
        if cur.val > val:
            cur.left = node
        else:
            cur.right = node
        return root