# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val==key:
            return self.helper(root)
        # if root.val==key:
        # to keep track of temp and to save
        temp=root
        while root:
            if root.val>key:
                if root.left and root.left.val==key: # checking wheter had we reachehd on the node we want to delete
                    root.left=self.helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right and root.right.val==key:   #checking wheter had we reachehd on the node we want to delete
                    root.right=self.helper(root.right)
                    break
                else:
                    root=root.right     #else keep tryinggg 
        return temp
    # here we check if single child(left,right) or both child are there
    def helper(self,root):
        if not root.left:  # only right child there
            return root.right
        elif not root.right:   #only left child there
            return root.left
        else:  
            
            rightchild=root.right   #here complete right side of tree is saved which we furthure add again /
            lastright=self.mostright(root.left)     # we retrieve rightmost element 
            lastright.right=rightchild   # we now create new tree with right side which we saved earlier
            return root.left
    # ye fun help krr rha hei right most element nikalne ke liye kyoki vo element will replace the deleted node
    def mostright(self,root):
        # if root.right:
        #     return None
        while root.right is not None :
            root=root.right
        return root

