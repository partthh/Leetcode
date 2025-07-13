# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        dep=0
        queue=deque([root])
        
        while queue:
            temp=[]
            len1=len(queue)
            dep+=1
            for i in range(len1):
                
                n1=queue.popleft()
                if n1.left:
                    queue.append(n1.left)
                if n1.right:
                    queue.append(n1.right)
            
        return dep

        