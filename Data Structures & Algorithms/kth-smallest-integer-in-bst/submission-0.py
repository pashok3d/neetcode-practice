# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # [4, 3, 5, 2, null]
        counter = 0
        found_num = None
        def dfs(node: Optional[TreeNode]): # 4, 5
            if not node:
                return
            dfs(node.left)
            nonlocal counter
            counter += 1 # 4
            if counter == k: # 4 == 4
                nonlocal found_num
                found_num = node.val
                return
            dfs(node.right) # dfs(5)

        dfs(root)
        return found_num


            