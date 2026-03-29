# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        found_non_balanced = False

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            height_node_left = height(node.left) + 1
            height_node_right = height(node.right) + 1
            if abs(height_node_left - height_node_right) > 1:
                nonlocal found_non_balanced
                found_non_balanced = True
            return max(height_node_left, height_node_right)

        height(root)
        return not found_non_balanced
        