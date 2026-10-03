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
class BSTIterator {
    Stack<TreeNode> s1=new Stack<TreeNode>();
    public void fun1(TreeNode temp){
        while(temp!=null){
            s1.push(temp);
            temp=temp.left;
        }
    }
    public BSTIterator(TreeNode root) {
        fun1(root); 
    }
    
    public int next() {
        TreeNode curr=s1.pop();
        fun1(curr.right);
        return curr.val;
    }
    
    public boolean hasNext() {
        return !s1.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */