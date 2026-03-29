# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        cur_max = None
        def func(node: Optional[TreeNode]) -> int: # 15
            if not node:
                return 0

            largest_left = func(node.left)
            largest_right = func(node.right)
            max_from_children = max(largest_left, largest_right)
            max_one_sided = max(max_from_children, 0) + node.val

            # check max path that goes into both sub-trees
            # and record it
            nonlocal cur_max
            cur_max = node.val if cur_max is None else max(cur_max, node.val)
            if node.left or node.right:
                cur_max = max(cur_max, max_one_sided)
                if node.left and node.right:
                    cur_max = max(cur_max, largest_left + node.val + largest_right)
                
            return max_one_sided

        func(root)

        return cur_max
