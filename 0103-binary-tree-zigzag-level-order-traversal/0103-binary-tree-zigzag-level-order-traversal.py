# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        leftToRight=True
        queue=deque([root])
        result=[]
        while queue:
            current=[]
            x=len(queue)
            for i in range(x):
                
                x1=queue.popleft()
                current.append(x1.val)
                if x1.left:
                    queue.append(x1.left)
                if x1.right:
                    queue.append(x1.right)
            if not leftToRight:
                current.reverse()
            
            result.append(current)
            leftToRight=not leftToRight
        return result

        