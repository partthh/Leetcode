# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.mini=float("-inf")
        self.maxi=float("inf")
    def helper(self,node,mini,maxi):
        if not node :
            return True
        if( not (mini<node.val<maxi)):
            return False
        return (self.helper(node.left,mini,node.val) and self.helper(node.right,node.val,maxi))
        # return True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root,self.mini,self.maxi)

        