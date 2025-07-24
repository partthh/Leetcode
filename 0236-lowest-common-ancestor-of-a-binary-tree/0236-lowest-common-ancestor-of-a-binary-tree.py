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
        if root is None or root==p or root==q:
            return root
        l1=self.lowestCommonAncestor(root.left,p,q)
        r1=self.lowestCommonAncestor(root.right,p,q)
        if not l1:
            return r1
        elif (not r1):
            return l1
        else:
            return root