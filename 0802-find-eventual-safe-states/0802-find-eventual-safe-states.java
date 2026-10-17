class Solution {
    public boolean fun1(int node,int[] vis,int[] pathvis,int[] res,int[][] graph){
        vis[node]=1;
        pathvis[node]=1;
        
        for(int x:graph[node]){
            if(vis[x]==0){
                if(fun1(x,vis,pathvis,res,graph)){
                    return true;
                }
            }   
            else if(pathvis[x]==1){
                return true;
            }
        }
        pathvis[node]=0;
        res[node]=1;
        return false;
    }
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int[] vis=new int[graph.length];
        int[] pathvis=new int[graph.length];
        int[] res=new int[graph.length];
        ArrayList<ArrayList<Integer>> adj=new ArrayList<>();
        for(int i=0;i<graph.length;i++){
            if(vis[i]==0){
                fun1(i,vis,pathvis,res,graph);
            }
        }
        List<Integer> ans=new ArrayList<>();
        for(int i=0;i<res.length;i++){
            if(res[i]==1){
                ans.add(i);
            }
        }
        return ans;
    }
}