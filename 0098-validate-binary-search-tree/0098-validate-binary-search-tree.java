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
    public boolean fun1(TreeNode temp,long min,long max){
        if(temp==null){
            return true;
        }
        if(temp.val>=max || temp.val<=min){
            return false;
        }
        return fun1(temp.left,min,temp.val) && fun1(temp.right,temp.val,max);
    }
    public boolean isValidBST(TreeNode root) {
        TreeNode temp=root;
        return fun1(temp,Long.MIN_VALUE,Long.MAX_VALUE) ;
    }
}