# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        curr=root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr=curr.right
            else:
                next1=curr.left
                while next1.right:
                    next1=next1.right
                next1.right=curr.right
                res.append(curr.val)
                curr=curr.left
        return res