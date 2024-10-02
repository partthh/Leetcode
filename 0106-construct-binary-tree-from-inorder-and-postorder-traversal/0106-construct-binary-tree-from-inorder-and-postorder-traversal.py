# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            indexx=inorder.index(postorder.pop())
            root=TreeNode(inorder[indexx])
            root.right=self.buildTree(inorder[indexx+1:],postorder)
            root.left=self.buildTree(inorder[:indexx],postorder)

            return root
            
        