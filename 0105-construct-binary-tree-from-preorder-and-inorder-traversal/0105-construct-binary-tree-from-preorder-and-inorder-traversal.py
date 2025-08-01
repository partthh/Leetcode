# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun1(self,preorder,inorder,start,end,dict1):
        if start>end:
            return None
        root=TreeNode(preorder[self.ind])
        # TreeNode.val=preorder[ind]
        i=dict1[root.val]
        self.ind+=1
        root.left=self.fun1(preorder,inorder,start,i-1,dict1)
        root.right=self.fun1(preorder,inorder,i+1,end,dict1)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        dict1={x:i for i,x in enumerate(inorder)}
        self.ind=0
        return self.fun1(preorder,inorder,0,len(preorder)-1,dict1)
