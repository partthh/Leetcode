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
    ArrayList<TreeNode> arr2 = new ArrayList<>();
    public ArrayList<TreeNode> inorder(TreeNode root){
        if(root==null){
            return arr2;
        }
        inorder(root.left);
        arr2.add(root);
        inorder(root.right);
        return arr2;
    }
    public boolean findTarget(TreeNode root, int k) {
        ArrayList<TreeNode> res=inorder(root);
        int left=0;
        int right=res.size()-1;
        while(left<right){
            if(res.get(left).val+res.get(right).val==k){
                return true;
            }
            if(res.get(left).val+res.get(right).val>k){
                right-=1;
            }
            else{
                left+=1;
            }
        }
        return false;
    }
}