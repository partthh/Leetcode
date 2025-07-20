# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        # if not root.left or not root.right:
            # return False
        return self.fun1(root.left,root.right)

    def fun1(self,t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val!=t2.val:
            return False
        return self.fun1(t1.left,t2.right) and self.fun1(t1.right,t2.left)