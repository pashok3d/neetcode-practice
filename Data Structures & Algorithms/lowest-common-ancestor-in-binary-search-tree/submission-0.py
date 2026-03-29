# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
# node such that p in left sub-tree and q in the right subtree
or
# node is p, and q in children
or
# node is q, and p in children
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smaller = p if p.val < q.val else q
        larger = q if q.val > p.val else p

        def func(node: Optional[TreeNode]):
            if node.val == smaller.val or node.val == larger.val:
                return node
            elif larger.val < node.val:
                # both in left sub-tree
                return func(node.left)
            elif smaller.val > node.val:
                # both in right sub-tree
                return func(node.right)
            else:
                # smaller in left sub-tree, larger in right subree
                return node

        return func(root)












