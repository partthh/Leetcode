# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        nodes=defaultdict(lambda: defaultdict(list))
        queue1=deque([(root,(0,0))])
        while queue1:
            temp,(x,y)=queue1.popleft()
            nodes[x][y].append(temp.val)
            if temp.left:
                queue1.append((temp.left,(x-1,y+1)))
            if temp.right:
                queue1.append((temp.right,(x+1,y+1)))
        result=[]
        for x in sorted( nodes.keys()):
            dummy=[]
            for y in sorted(nodes[x].keys()):
                dummy.extend(sorted(nodes[x][y]))
            result.append(dummy)
        return result

        