# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        return self.candidate(root,subRoot)

    def candidate(self,root,subroot):

        if not root or not subroot:
            return False

        if root.val == subroot.val:
            current = self.dfs(root,subroot)
            if current:
                return current
        
        
        
        left = self.candidate(root.left,subroot)
        right = self.candidate(root.right,subroot)

        if left:
            return left
        elif right:
            return right
        else:
            return False

    def dfs(self,root,subroot):

        if not root and not subroot:
            return True
        
        if not root or not subroot:
            return 

        if root.val == subroot.val:
            right = self.dfs(root.right,subroot.right)
            left = self.dfs(root.left,subroot.left)
            if right and left:
                return True
            else:
                return False

        

