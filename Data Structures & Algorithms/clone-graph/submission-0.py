"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_2_new = {}

        if not node:
            return None
        
        # traverse node

        def dfs(node):
            if node not in old_2_new:
                old_2_new[node] = Node(node.val)
            for n in node.neighbors:
                if n not in old_2_new:
                    old_2_new[n] = Node(n.val)
                    dfs(n)
                if old_2_new[n] not in old_2_new[node].neighbors:
                    old_2_new[node].neighbors.append(old_2_new[n])
                

        dfs(node)

        return old_2_new[node]
        