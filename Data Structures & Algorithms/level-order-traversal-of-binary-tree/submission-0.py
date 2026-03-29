# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        cur_level = 0
        cur_list = []
        d = deque()

        d.append((root, cur_level))

        while d:
            node, lvl = d.popleft()
            if cur_level != lvl:
                # we are at the next level
                # flush 
                result.append(cur_list)
                cur_level += 1
                cur_list = []

            cur_list.append(node.val)

            if node.left is not None:
                d.append((node.left, cur_level+1))
            if node.right is not None:
                d.append((node.right, cur_level+1))
        
        if cur_list:
           result.append(cur_list) 
        return result
        