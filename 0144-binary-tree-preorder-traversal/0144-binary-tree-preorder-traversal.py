# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder=[]
        if root is None:
            return preorder
        l1=[]
        l1.append(root)
        while l1:
            root=l1.pop()
            preorder.append(root.val)
            if root.right:
                l1.append(root.right)
            if root.left:
                l1.append(root.left)
        return preorder


        