# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=1
        if not root:
            return 0
        queue=deque([[root,0]])
        # first,last=None,None
        while queue:
            len1=len(queue)
            usele,mini=queue[0]
            for i in range(len1):
                node,index=queue.popleft()
                curr_index=index-mini
                if i==0:
                    first=curr_index
                if i==len1-1:

                    last=curr_index
                if node.left:
                    queue.append([node.left,2*curr_index+1])
                if node.right:
                    queue.append([node.right,2*curr_index+2])
            res=max(res,last-first+1)
        return res