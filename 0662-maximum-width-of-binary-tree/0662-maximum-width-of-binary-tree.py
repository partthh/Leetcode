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
        if not root:
            return 0
        maxi=1
        queue=deque([[root,0]])
        while queue:
            l1=len(queue)
            useless,mini=queue[0]
            for i in range(l1):
                curr,index=queue.popleft()
                curr_no=index-mini
                if i==0:
                    first=curr_no
                if i==l1-1:
                    last=curr_no
                if curr.left:
                    queue.append([curr.left,2*curr_no+1])
                if curr.right:
                    queue.append([curr.right,2*curr_no+2])
            maxi=max(maxi,last-first+1)
        return maxi  