class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n=isConnected.length;
        boolean[] vis=new boolean[n];

        ArrayList<ArrayList<Integer>> res=new ArrayList<>();
        for(int i=0;i<n;i++){
            if(!vis[i]){            
                ArrayList<Integer> temp=new ArrayList<>();
                dfs(i,isConnected,vis,temp);
                res.add(temp);
            }
        
    }
    return res.size();

}
public void dfs(int node ,int[][]isConnected,boolean[] vis,ArrayList<Integer> temp)
{
    vis[node]=true;
    temp.add(node);
    for(int i=0;i<isConnected.length;i++){
        if(!vis[i] && isConnected[node][i]==1){
            dfs(i,isConnected,vis,temp);
        }
    }
}
}