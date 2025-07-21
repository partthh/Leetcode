# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res=[]
        self.fun1(root,[],res)
        return res
    def fun1(self,root,temp,res):
        if not root:
            return
        temp.append(str(root.val))
        if not root.left and not root.right:
            res.append("->".join(temp))
        else:
            self.fun1(root.left,temp,res)
            self.fun1(root.right,temp,res)
        temp.pop()
    

        