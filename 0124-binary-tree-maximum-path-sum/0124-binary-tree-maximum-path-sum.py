# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi=float('-inf')
        self.fun1(root)
        return self.maxi
    def fun1(self,root):
        if not root:
            return 0
        l1=max(0,self.fun1(root.left))
        r1=max(0,self.fun1(root.right))
        self.maxi=max(self.maxi,l1+r1+root.val)
        return root.val+max(l1,r1)
