# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun1(self,root,count):
        if not root:
            return 0
        
        l1=self.fun1(root.left,count)
        r1=self.fun1(root.right,count)
        return 1+l1+r1
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        return self.fun1(root,count)
        