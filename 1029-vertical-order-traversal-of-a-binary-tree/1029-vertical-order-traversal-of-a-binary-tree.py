# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        nodes=defaultdict(lambda:defaultdict(list))
        res=[]

        queue=deque([(root,(0,0))])
        while queue:
            temp,(x,y)=queue.popleft()
            nodes[x][y].append(temp.val)
            if temp.left:
                queue.append((temp.left,(x-1,y+1)))
            if temp.right:
                queue.append((temp.right,(x+1,y+1)))

        for x in sorted(nodes):
            temp=[]
            for y in sorted (nodes[x]):
                temp.extend(sorted(nodes[x][y]))
            res.append(temp)
        return res
