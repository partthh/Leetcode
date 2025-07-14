# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.fun1(root)!=-1
    def fun1(self,root):
        if not root:
            return 0
        l1=self.fun1(root.left)
        if l1==-1:
            return -1
        r1=self.fun1(root.right)
        if r1==-1:
            return -1
        if abs(l1-r1)>1:
            return -1
        return 1+max(l1,r1)
    
        