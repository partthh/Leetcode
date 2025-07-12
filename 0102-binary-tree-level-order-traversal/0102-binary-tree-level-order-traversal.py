# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=deque([root])
        res=[]
        while queue:
            temp=[]
            len1=len(queue)
            for i in range(len1):
                n1=queue.popleft()
                # print(n1.val)
                temp.append(n1.val)
                if n1.left:
                    queue.append(n1.left)
                if n1.right:
                    queue.append(n1.right)
            res.append(temp)
        return res
