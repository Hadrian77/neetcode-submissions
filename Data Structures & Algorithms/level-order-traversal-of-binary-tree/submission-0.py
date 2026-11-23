# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        lis = []
        q.append(root)
        print(len(q))

        while len(q) > 0:
            
            innerLis = []
            for i in range(len(q)):
                
                
                current = q.popleft()

                if current:
                    innerLis.append(current.val)

                    if current.left:
                        q.append(current.left)
                    
                    if current.right:
                        q.append(current.right)
            
            if innerLis:
                lis.append(innerLis)
        

        return lis
