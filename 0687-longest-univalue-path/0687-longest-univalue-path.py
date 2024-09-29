# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # maxi=[0]
        self.maxi=0
        
        # return maxi[0]
        def height(root,parent):
            if not root:
                return 0
            lh=height(root.left,root.val)
            rh=height(root.right,root.val)

            self.maxi=max(self.maxi,lh+rh)
            return 1+max(lh,rh) if root.val==parent else 0
        height(root,None)
        return self.maxi