"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        mapping = defaultdict(Node)
        start = node
        
        def dfs(node):
            mapping[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in mapping:
                    dfs(neighbor)
        dfs(start)

        for oldNode in mapping:
            for neighbor in oldNode.neighbors:
                mapping[oldNode].neighbors.append(mapping[neighbor])
                
        return mapping[start]



        
        
        
        