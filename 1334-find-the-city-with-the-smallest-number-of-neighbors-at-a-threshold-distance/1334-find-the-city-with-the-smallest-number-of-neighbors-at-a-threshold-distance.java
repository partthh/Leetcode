class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] adj=new int[n][n];
        for(int i=0;i<n;i++){
            Arrays.fill(adj[i],Integer.MAX_VALUE);
            adj[i][i]=0;
        }
        for(int[] edge:edges){
            int u=edge[0];
            int v=edge[1];
            int w=edge[2];

            adj[u][v]=Math.min(adj[u][v],w);
            adj[v][u]=Math.min(adj[u][v],w);

        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    if(adj[j][i]!=Integer.MAX_VALUE && adj[i][k]!=Integer.MAX_VALUE){
                        adj[j][k]=Math.min(adj[j][k],adj[j][i]+adj[i][k]);
                    }
                }
            }
        }
        int ans=-1;
        int best=Integer.MAX_VALUE;
        int curr=0;
        for(int i=0;i<n;i++){
            curr=0;
            for(int j=0;j<n;j++){
                if(i!=j && adj[i][j]<=distanceThreshold){
                    curr+=1;
                }
            }
            if(curr<=best){
                best=curr;
                ans=i;
            }
        }
        return ans;
    }
}