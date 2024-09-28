# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.arr=[]
    def fun1(self,node,level):
        if not node:
            return None
        
        if len(self.arr)==level:
            self.arr.append(node.val)
        self.fun1(node.right,level+1)
        self.fun1(node.left,level+1)
            
        return self.arr
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.fun1(root,0)