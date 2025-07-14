# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        l1=self.fun1(root.left)
        r1=self.fun1(root.right)
        if abs(l1-r1)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def fun1(self,root):
        if not root:
            return 0
        queue=deque([root])
        dept=0
        while queue:
            
            len1=len(queue)
            # dept+=1
            for i in range(len1):
                n1=queue.popleft()
                if n1.left:
                    queue.append(n1.left)
                if n1.right:
                    queue.append(n1.right)
            dept+=1
        return dept


        