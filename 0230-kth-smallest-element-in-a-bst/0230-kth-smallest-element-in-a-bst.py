# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans=[]
    def helper(self,root):
        if not root:
            return None
        
        self.helper(root.left)
        self.ans.append(root.val)
        self.helper(root.right)
            # elif( root.right):
            #     root=self.kthSmallest(root.right,k)
        return self.ans
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # ans=set()
        if not root:
            return None
        arr1=[]
        arr1=self.helper(root)
        arr1.sort()
        x=arr1[k-1]
        return x