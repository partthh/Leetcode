# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        sum1=root.val
        sum2=0
        if root.left:
            sum2+=root.left.val
        if root.right:
            sum2+=root.right.val
        return sum1==sum2
        #     return True
        # else:
        #     return False
        # self.checkTree(root.left) and self.checkTree(root.right)

        