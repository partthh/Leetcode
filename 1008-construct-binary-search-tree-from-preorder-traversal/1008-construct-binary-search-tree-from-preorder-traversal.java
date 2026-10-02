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
    public TreeNode bstFromPreorder(int[] preorder) {
        TreeNode root=new TreeNode(preorder[0]);
        for(int i=1;i<preorder.length;i++){
            fun1(root,preorder[i]);
        }
        return root;
    }
    public void fun1(TreeNode root,int value){
        if(root.val>value){
            if(root.left==null){
                root.left=new TreeNode(value);
            }
            else{
                fun1(root.left,value);
            }
        }
        else{
            if(root.right==null){
                root.right=new TreeNode(value);
            }
            else{
                fun1(root.right,value);
            }
        }
    }
}