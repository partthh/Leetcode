# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxi = [float('-inf')]
        # maxi=float("-inf")
        self.sum1(root,maxi)
        return maxi[0]
    def sum1(self,root,maxi):
        if not root:
            return 0
        leftsum=max(0,self.sum1(root.left,maxi))
        rightsum=max(0,self.sum1(root.right,maxi))
        maxi[0]=max(maxi[0],leftsum+rightsum+root.val)
        return root.val+max(leftsum,rightsum)
    