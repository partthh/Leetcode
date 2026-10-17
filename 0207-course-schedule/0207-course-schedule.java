class Solution {
    public boolean dfs(int node,ArrayList<ArrayList<Integer>> adj,int[] vis,int[] pathvis){
        vis[node]=1;
        pathvis[node]=1;
        for(int a:adj.get(node)){
            if(vis[a]==0){
                if(dfs(a,adj,vis,pathvis)){
                    return true;
                }
            
            }
            else if(pathvis[a]==1){
                return true;
            }
        }
        pathvis[node]=0;
        return false;

    }
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj=new ArrayList<>();
        for(int i=0;i<numCourses;i++){
            adj.add(new ArrayList<>());
        }
        for(int[] i:prerequisites){
            int u=i[0];
            int v=i[1];
            adj.get(v).add(u);
        }
        int[] vis=new int[numCourses];
        int[] pathvis=new int[numCourses];
        for(int i=0;i<numCourses;i++){
            if(vis[i]==0){
                if(dfs(i,adj,vis,pathvis)){
                    return false;
                }
            }
        }
        return true;
    }
}