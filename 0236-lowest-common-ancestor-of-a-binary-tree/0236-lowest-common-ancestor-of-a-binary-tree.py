# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res=[]
        res1=[]
        self.fun1(root,res,p)
        self.fun1(root,res1,q)
        print([node.val for node in res])
        print([node.val for node in res1])
        i=0
        # if len(res)==2:
            # return res[0]
        while i<len(res) and i<len(res1) and res[i]==res1[i]:
            i+=1
        return res[i-1]
        # print(i)
        # if len(res)>len(res1):
# 
            # return res[i]
        # else:
            # return res1[i]
    def fun1(self,root,res,tar):
        if not root:
            return False
        res.append(root)
        if root==tar:

            return True
        if self.fun1(root.left,res,tar) or self.fun1(root.right,res,tar):
            return True
        # else:
        #     self.fun1(root.left,res,tar)
        #     self.fun1(root.right,res,tar)
        res.pop()
        return False

        