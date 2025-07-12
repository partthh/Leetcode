# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        st=[]
        if not root:
            return []
        st.append(root)
        while st:
            ele=st.pop()
            result.append(ele.val)
            if ele.right:
                st.append(ele.right)
            if ele.left:
                st.append(ele.left)
        return result