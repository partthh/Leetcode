# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        if root.left.val!=root.right.val:
            return False
        x1=self.fun1(root.left) 
        x2=self.fun1(root.right)
        for i in range(len(x2)):
            x2[i].reverse()
        if x1!=x2:
            return False
        return True
    
    def fun1(self,root):
        if not root:
            return []
        queue=deque([root])
        res=[]
        while queue:
            l1=len(queue)
            temp=[]
            for i in range(l1):
                n1=queue.popleft()
                if n1:

                    temp.append(n1.val)
                    queue.append(n1.left)
                    queue.append(n1.right)
                else:
                    temp.append(None)

                # if n1.left:
                #     queue.append(root.left)
                # if n1.right:
                #     queue.append(root.left)
            res.append(temp)
        return res
