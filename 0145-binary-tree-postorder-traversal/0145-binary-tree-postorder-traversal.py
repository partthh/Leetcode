# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        s1=[]
        curr=root
        res=[]
        while curr!=None or len(s1)!=0:
            if curr !=None:
                s1.append(curr)
                curr=curr.left
            else:
                node=s1[-1]
                temp=node.right
                if temp==None:
                    temp=s1.pop()
                    res.append(temp.val)
                    while (len(s1)!=0 and temp==s1[-1].right ):
                        temp=s1.pop()
                        res.append(temp.val)
                else:
                    curr=temp

        return res