# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root,parent_map):

        if not root:
            return
        if root.left:
            parent_map[root.left]=root
            self.inorder(root.left,parent_map)
        if root.right:
            parent_map[root.right]=root
            self.inorder(root.right,parent_map)
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        parent_set={}
        self.inorder(root,parent_set)
        visited=set()
        visited.add(target)
        queue=deque([target])
        level=0
        res=[]
        while queue:
            if level==k:
                break
            len1=len(queue)
            for i in range(len1):
                node=queue.popleft()
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node in parent_set and parent_set[node] not in visited:
                    queue.append(parent_set[node])
                    visited.add(parent_set[node])
            level+=1

        for i in queue:
            res.append(i.val)
        return res

