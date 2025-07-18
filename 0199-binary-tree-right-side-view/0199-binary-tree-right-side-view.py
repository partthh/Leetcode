# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        res=[]
        res1=[]
        queue=deque([root])
        while queue:
            len1=len(queue)
            temp=[]
            for i in range(len1):
                n1=queue.popleft()
                temp.append(n1.val)
                if n1.left:
                    queue.append(n1.left)
                if n1.right:
                    queue.append(n1.right)
            res.append(temp)
        # print
        for i in range(len(res)):
            res1.append(res[i][-1])
        return res1

        