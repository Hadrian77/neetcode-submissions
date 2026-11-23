# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(root,result):
            if not root:
                result.append("")
                return
            
            result.append(str(root.val))

            dfs(root.left,result)
            dfs(root.right,result)

        dfs(root,result)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        result = data.split(',')

        def dfs(result):
            if not result[0]:
                result.pop(0)
                return None
            
            current = TreeNode(val=result.pop(0))
            current.left = dfs(result)
            current.right = dfs(result)
            
            return current

        return dfs(result)

