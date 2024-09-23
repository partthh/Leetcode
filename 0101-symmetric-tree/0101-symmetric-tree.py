# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isTreeSymmetric(root.left,root.right)
    def isTreeSymmetric(self,leftroot,rightroot):
        # leftroot=root.left
        # rightroot=root.right
        if not leftroot and not rightroot:
            return True
        if ((not leftroot or not rightroot)):
            return False
        if leftroot.val!=rightroot.val:
            return False

        return self.isTreeSymmetric(leftroot.left,rightroot.right) and self.isTreeSymmetric(leftroot.right,rightroot.left)
        