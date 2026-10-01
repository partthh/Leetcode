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
    public TreeNode fun1(TreeNode root1){
        if(root1.left==null){
            return root1.right;
        }
        if(root1.right==null){
            return root1.left;
        }
        TreeNode x2=root1.right;
        while(x2.left!=null){
            x2=x2.left;
        }
        x2.left=root1.left;
        return root1.right;
    }
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null){
            return null;
        }
        if(root.val==key){
            return fun1(root);
        }
        TreeNode temp= root;
        while(temp!=null){
            if(temp.left!=null && temp.left.val==key){
                temp.left=fun1(temp.left);
                break;
            }
            if(temp.right!=null && temp.right.val==key){
                temp.right=fun1(temp.right);
                break;
            }
            if(key>temp.val){
                temp=temp.right;
            }
            else{
                temp=temp.left;
            }
            
    }
    return root;
    }
}