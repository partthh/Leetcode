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
        :type root: TreeNode
        :rtype: int
        """
        level=[]
        
        if not root :
            return 0
        
        queue=deque([root])
        while queue:
            current=[]
            n=len(queue)
            for i in range(n):
                x1=queue.popleft()
                current.append(x1.val)

                if x1.left:
                    queue.append(x1.left)

                if x1.right:
                    queue.append(x1.right)
            level.append(current)
        return len(level)
