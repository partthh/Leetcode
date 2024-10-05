# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root==q or root==p:
            return root
        leftt=self.lowestCommonAncestor(root.left,p,q)
        rightt=self.lowestCommonAncestor(root.right,p,q)
        if leftt is None:
            return rightt
        if rightt is None:
            return leftt
        else:
            return root
        