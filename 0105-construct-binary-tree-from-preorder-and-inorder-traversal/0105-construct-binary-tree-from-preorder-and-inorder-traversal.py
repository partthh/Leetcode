# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution(object):
    # def helper(self,inorder_s,inorder_e,preorder_s,preorder_e):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            iindex=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[iindex])
            root.left= self.buildTree(preorder,inorder[:iindex])
            root.right=self.buildTree(preorder,inorder[iindex+1:])
            return root
        #     inorder=inorder[:iindex]
        #     preorder=preorder[]
        #     buildTree(,inorder)

        # arr=[]
        # if not preorder :
        #     return []
        # arr[element] = 
        

        