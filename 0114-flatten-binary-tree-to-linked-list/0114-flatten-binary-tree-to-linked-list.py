# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def fun1(self,root):

        if not root:
            return []
        curr=root
        res=[]
        while curr:
            if not curr.left:
                res.append(curr)
                curr=curr.right
            else:
                next1=curr.left
                while next1.right:
                    next1=next1.right
                res.append(curr)
                next1.right=curr.right
                curr=curr.left
        return res
    def fun2(self,res):
        if not res:
            return None
        root=TreeNode(res[0])
        current=root
        for i in res[1:]:
            current.right=TreeNode(i)
            current=current.right
        return root
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        arr=self.fun1(root)
        if not arr:
            return 
        for i in range(len(arr)-1):
            arr[i].left=None
            arr[i].right=arr[i+1]
        # if arr:
        arr[-1].left=None
        arr[-1].right=None
        


                