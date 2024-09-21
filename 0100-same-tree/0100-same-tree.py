# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # l1=[]
        # l2=[]
        # if p:
        #     l2.append(p.val)
        #     self.isSameTree(p.left)
        #     self.isSameTree(p.right)
        
        # if q:
        #     l2.append(q.val)
        #     self.isSameTree(q.left)
        #     self.isSameTree(q.right)
        
        return (p.val==q.val and
                self.isSameTree(p.left,q.left) and
                self.isSameTree(p.right,q.right))

        
        