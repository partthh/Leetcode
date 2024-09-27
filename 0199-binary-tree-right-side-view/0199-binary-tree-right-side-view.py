# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def __init__(self):
        self.arr=[]

    def height(self,root):
        if not root:
            return 0
        
        lh=self.height(root.left)
        rh=self.height(root.right)
        return 1+ max(lh,rh) 
    def fun(self,node,level):
        if not node:
            return None
        if (len(self.arr)==level):
            self.arr.append(node.val)
        self.fun(node.right,level+1)
        self.fun(node.left,level+1)
        return self.arr
        
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.fun(root,0)
        
        
        