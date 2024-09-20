# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack1=[]
        stack2=[]
        postorder=[]

        stack1.append(root)
        if root is None:
            return postorder
        while stack1:
            x1=stack1.pop()
            stack2.append(x1.val)
            if x1.left:
                stack1.append(x1.left)

            if x1.right:
                stack1.append(x1.right)
            
        while stack2:
            postorder.append(stack2.pop())
        return postorder









        