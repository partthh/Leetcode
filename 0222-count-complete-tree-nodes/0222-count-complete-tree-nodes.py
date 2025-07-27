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
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        dict1={}
        self.fun1(root,dict1)
        visited=set()
        visited.add(root)
        queue=deque([root])

        while queue:
            len1=len(queue)
            for i in range(len1):
                node=queue.popleft()
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node in dict1 and dict1[node] not in visited:
                    queue.append(dict1[node])
                    visited.append(dict1[node])
        return len(visited)

        