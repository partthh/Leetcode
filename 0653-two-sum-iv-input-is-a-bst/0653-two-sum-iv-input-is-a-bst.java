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
 public class iterator{
    Stack<TreeNode> s1=new Stack<TreeNode>();
    Boolean reverse=true;
    public iterator(TreeNode root,boolean isreverse){
        reverse=isreverse;
        fun1(root);
    }
    public void fun1(TreeNode root){
        while(root!=null){
            s1.push(root);
            if(reverse){
                root=root.right;
            }
            else{
                root=root.left;
            }
    }

 }
    public int next(){
        TreeNode temp=s1.pop();
        if(reverse){
            fun1(temp.left);
        }
        else{
            fun1(temp.right);
        }
        return temp.val;
    }
 }
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        iterator l=new iterator(root, false);
        iterator r=new iterator(root,true);
        int left=l.next();
        int right=r.next();
        while(left<right){
            if(left+right==k){
                return true;
            }
            else if(left+right<k){
                left=l.next();
            }
            else{
                right=r.next();
            }
        }
        return false;
    }
}