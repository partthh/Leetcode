# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """    
        curr=root
        while curr:
            if curr.left:
                next1=curr.left
                while next1.right:
                    next1=next1.right
                next1.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right


                