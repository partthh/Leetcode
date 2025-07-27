# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def fun1(self,root,dict1):
        if not root:
            return 
        if root.left :
            dict1[root.left]=root
            self.fun1(root.left,dict1)
        if root.right:
            dict1[root.right]=root
            self.fun1(root.right,dict1)
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # if not root:
            # return 
        dict1={}
        self.fun1(root,dict1)
        vis=set()
        vis.add(target)
        queue=deque([target])
        level=0
        while queue:
            if level==k:
                break
            len1=len(queue)
            for i in range(len1):
                n1=queue.popleft()

                if n1.left and n1.left not in vis:
                    queue.append(n1.left)
                    vis.add(n1.left)
                if n1.right and n1.right not in vis:
                    queue.append(n1.right)
                    vis.add(n1.right)
                if n1 in dict1 and dict1[n1] not in vis:
                    queue.append(dict1[n1])
                    vis.add(dict1[n1])

            level+=1
        return [i.val for i in queue]
