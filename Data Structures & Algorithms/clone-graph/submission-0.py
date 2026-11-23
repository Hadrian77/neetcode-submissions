"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        cache = {}
        return self.clone(node,cache)
        
    def clone(self,node,cache):

        if not node:
            return None

        if node in cache:
            return cache[node]
        
        new = Node(node.val,[])
        cache[node] = new

        for neighbor in node.neighbors:
            new.neighbors.append(self.clone(neighbor,cache))

        return new

            