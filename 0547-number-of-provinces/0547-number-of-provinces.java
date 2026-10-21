class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n=isConnected.length;
        boolean[] vis=new boolean[n];
        int count=0;
        ArrayList<ArrayList<Integer>> res=new ArrayList<>();
        for(int i=0;i<n;i++){
            if(!vis[i]){            
                dfs(i,isConnected,vis);
                count+=1;
            }
        
    }
    return count;

}
public void dfs(int node ,int[][]isConnected,boolean[] vis)
{
    vis[node]=true;
    for(int i=0;i<isConnected.length;i++){
        if(!vis[i] && isConnected[node][i]==1){
            dfs(i,isConnected,vis);

        }
    }
}
}