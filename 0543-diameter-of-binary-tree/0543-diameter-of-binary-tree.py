# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def __init__(self):
        # self.maxi=0
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # if not root:
            # return 0
        self.maxi=0
        self.fun1(root)
        return self.maxi

        # l1=self.diameterOfBinaryTree(root.left)
        # r1=self.diameterOfBinaryTree(root.right)

        # self.maxi=max(self.maxi,l1+r1)

        # return 1+max(l1,r1)
        
    def fun1(self,root):
        if not root:
            return 0
        l1=self.fun1(root.left)
        r1=self.fun1(root.right)
        self.maxi=max(self.maxi,l1+r1)
        return max(l1,r1)+1