# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderDict = {}

        for x in range(len(inorder)):
            inorderDict[inorder[x]] = x
    
        return self.build(preorder,inorderDict)
    


    def build(self,preorder:List[int],inorderDict)-> Optional[TreeNode]:

        if not preorder:
            return None

        node = TreeNode(preorder[0])
        leftList = []
        rightList = []

        for x in range(1,len(preorder)):

            if inorderDict[preorder[x]] > inorderDict[preorder[0]]:
                rightList.append(preorder[x])
            else:
                leftList.append(preorder[x])


        node.left = self.build(leftList,inorderDict)
        node.right = self.build(rightList,inorderDict)

        return node