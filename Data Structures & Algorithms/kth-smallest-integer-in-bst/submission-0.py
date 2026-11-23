# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        global val,counter
        val = 0
        counter = 0
        self.search(root,k)
        print('Return value = ', val)
        return val



    def search(self,root: Optional[TreeNode],k:int):    

        global counter,val

        if not root:
            return

        self.search(root.left,k)

        counter += 1
        print('Counter = ', counter)
        if counter == k:
            val = root.val
            print('Val = ',val)
            print('K = ', k)
            print('Root.val = ', root.val)
        
        self.search(root.right,k)

        