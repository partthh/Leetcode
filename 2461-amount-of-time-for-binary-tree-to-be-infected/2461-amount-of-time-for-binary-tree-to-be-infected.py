# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun1(self,root,dict1):
        if not root:
            return
        if root.left:
            dict1[root.left]=root
            self.fun1(root.left,dict1)
        if root.right:
            dict1[root.right]=root
            self.fun1(root.right,dict1)
    def fun2(self,root,start):
        if not root:
            return None
        if root.val==start:
            return root
        l1=self.fun2(root.left,start)
        if l1:
            return l1
        r1=self.fun2(root.right,start)
        if r1:
            return r1

    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        count=-1
        dict1={}
        self.fun1(root,dict1)
        start1=self.fun2(root,start)
        visited=set()
        visited.add(start1)
        queue=deque([start1])
        while queue:
            len1=len(queue)
            count+=1
            for i in range(len1):
                node=queue.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                if node in dict1 and dict1[node] not in visited:
                    visited.add(dict1[node])
                    queue.append(dict1[node])
            
                
        return count