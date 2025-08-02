# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
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
                prev=curr.left
                while prev.right:
                    prev=prev.right
                prev.right=curr
                temp=curr
                curr=curr.left
                temp.left=None
        return res