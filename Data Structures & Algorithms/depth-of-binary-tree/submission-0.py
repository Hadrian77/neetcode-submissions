# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dive(root)
    def dive(self,root):

        if not root:
            return 0
        

        
        return max(self.dive(root.left) + 1,self.dive(root.right) + 1)