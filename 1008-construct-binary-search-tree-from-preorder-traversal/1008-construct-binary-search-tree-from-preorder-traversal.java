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
    HashMap<Integer,Integer> h1=new HashMap<>();
    int preindex=0;
    public TreeNode bstFromPreorder(int[] preorder) {
        int[] inorder=preorder.clone();
        Arrays.sort(inorder);
        for(int i=0;i<preorder.length;i++){
            h1.put(inorder[i],i);
        }
        return fun1(preorder,0,preorder.length-1);
    }
    public TreeNode fun1(int[] preorder,int start, int end){
        if(start>end){
            return null;
        }
        int rootvalue=preorder[preindex++];
        TreeNode root=new TreeNode(rootvalue);
        int pos=h1.get(rootvalue);
        root.left=fun1(preorder,start,pos-1);
        root.right=fun1(preorder,pos+1,end);
        return root;
    }
}