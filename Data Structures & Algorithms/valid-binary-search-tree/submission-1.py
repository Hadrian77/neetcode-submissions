# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(root, low, high):

            if not root:
                return True

            if low < root.val < high:

                left = check(root.left,low,root.val)
                right = check(root.right,root.val,high)
                return left and right

            else:
                return False
        
        return check(root,float("-inf"),float("inf"))