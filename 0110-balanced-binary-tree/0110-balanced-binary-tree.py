# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lh=self.height(root.left)
        rh=self.height(root.right)
        if (abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)):
            return True
        return False  
    def height(self,root):
    # def height(self,root):
        if not root:
            return 0
        lh=self.height(root.left)
        rh=self.height(root.right)
        return max(lh,rh)+1  
    