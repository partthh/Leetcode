# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=deque([root])
        res=[]
        x1=False
        while queue:
            temp=[]
            n=len(queue)
            
            for i in range(n):

                n1=queue.popleft()
                temp.append(n1.val)
                if n1.left:
                    queue.append(n1.left)
                if n1.right:
                    queue.append(n1.right)
            if x1:
                temp.reverse()
            res.append(temp)
            if x1:
                x1=False
            else:
                x1=True

        return res

        