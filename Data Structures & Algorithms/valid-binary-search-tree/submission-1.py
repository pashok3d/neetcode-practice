# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def bst(node: TreeNode) -> Tuple[int, int, bool]:
            if node.left and node.right:
                left_max, left_min, is_left_bst = bst(node.left)
                right_max, right_min, is_right_bst = bst(node.right)
                is_bst = is_left_bst and is_right_bst and left_max < node.val and right_min > node.val 
                return [right_max, left_min, is_bst]
            elif node.left:
                # node has only left child
                left_max, left_min, is_left_bst = bst(node.left)
                is_bst = is_left_bst and left_max < node.val 
                return [node.val, left_min, is_bst]
            elif node.right:
                # node has only right child
                right_max, right_min, is_right_bst = bst(node.right)
                is_bst = is_right_bst and right_min > node.val
                return [right_max, node.val, is_bst]
            else:
                return [node.val, node.val, True]

        return bst(root)[-1]
