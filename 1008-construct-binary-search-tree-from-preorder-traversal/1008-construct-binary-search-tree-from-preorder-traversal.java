/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int index=0;
    public TreeNode bstFromPreorder(int[] preorder) {
        index=0;
        return fun1(Integer.MAX_VALUE,preorder);
    }
    public TreeNode fun1(int upper,int[] preorder){
        if(index==preorder.length || preorder[index]>upper){
            return null;
        }
        TreeNode root=new TreeNode(preorder[index++]);
        root.left=fun1(root.val,preorder);
        root.right=fun1(upper,preorder);
        return root;
    }
}