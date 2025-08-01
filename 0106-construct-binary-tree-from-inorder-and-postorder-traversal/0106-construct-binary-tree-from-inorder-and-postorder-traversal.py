# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun1(self,postorder,inorder,start,end,dict1):
        if start>end:
            return None
        root=TreeNode(postorder[self.ind])
        # TreeNode.val=preorder[ind]
        i=dict1[root.val]
        self.ind-=1
        root.right=self.fun1(postorder,inorder,i+1,end,dict1)
        
        root.left=self.fun1(postorder,inorder,start,i-1,dict1)
        return root
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        dict1={x:i for i,x in enumerate(inorder)}
        self.ind=len(postorder)-1
        return self.fun1(postorder,inorder,0,len(postorder)-1,dict1)