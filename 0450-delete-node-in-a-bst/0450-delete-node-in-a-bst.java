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
    public TreeNode fun1(TreeNode temp){
        if(temp.left==null){
            return temp.right;
        }
        if(temp.right==null){   
            return temp.left;
        }
        TreeNode last=temp.right;
        while(last.left!=null){
            last=last.left;
        }
        last.left=temp.left;
        return temp.right;

    }
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null){
            return root;
        }
        if(root.val==key){
            return fun1(root);
        }
        TreeNode temp=root;
        while(temp!=null){
            if(temp.left!=null && temp.left.val==key){
                temp.left=fun1(temp.left);
                break;
            }
            if(temp.right!=null && temp.right.val==key){
                temp.right=fun1(temp.right);
                break;
            }
            if(key<temp.val){
                temp=temp.left;
            }
            else{
                temp=temp.right;
            }
        }
        return root;

    }
}