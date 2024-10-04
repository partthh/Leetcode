# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans=0
        self.result=None
    def helper(self,root,k):
        if not root or self.result is not None:
            return None

        self.helper(root.left,k)
        # (root.val)
        self.ans+=1
        if self.ans==k:
            self.result=root.val
            return 
        self.helper(root.right,k)
        # return -1
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # ans=set()
        if not root:
            return None
        # arr1=[]
        # count=1
        self.helper(root,k)

        return self.result