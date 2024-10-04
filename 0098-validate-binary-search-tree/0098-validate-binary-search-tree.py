# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.arr=[]
    def helper(self,root):
        if not root:
            return None
        self.helper(root.left)
        self.arr.append(root.val)
        self.helper(root.right)
    def issorted(self):
        for i in range(len(self.arr)-1):
            if not( self.arr[i]<self.arr[i+1]):
                return False
        return True
                

        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False

        self.helper(root)
        if(self.issorted()):
            return True
        else:
            return False

        