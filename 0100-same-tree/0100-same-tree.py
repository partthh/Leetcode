# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val!=q.val:
        #     return False
        self.p=[]
        self.q=[]
        self.fun1(p,self.p)
        self.fun1(q,self.q)
        return self.p==self.q
    def fun1(self,root,arr):
        if not root:
            arr.append(None)
            return 
        arr.append(root.val)
        self.fun1(root.left,arr)
        self.fun1(root.right,arr)

        