    class Solution {
        public boolean dfs(int node,ArrayList<ArrayList<Integer>> adj,Stack<Integer> s1,int[] vis,int[] pathvis){
            vis[node]=1;
            pathvis[node]=1;
            for(int i:adj.get(node)){
                if(vis[i]==0){
                    if(dfs(i,adj,s1,vis,pathvis)){
                        return true;
                    }
                }
                else if(pathvis[i]==1){
                    return true;
                }
            }
            pathvis[node]=0;
            s1.push(node);
            return false;
        }
        public int[] findOrder(int numCourses, int[][] prerequisites) {
            int[] res=new int[numCourses];
            int[] vis=new int[numCourses];
            int[] pathvis=new int[numCourses];
            Stack<Integer> s1=new Stack<>();
            ArrayList<ArrayList<Integer>> adj=new ArrayList<>();
            for(int i=0;i<numCourses;i++){
                adj.add(new ArrayList<>());
            }
            for(int[] i:prerequisites){
                int u=i[0];
                int v=i[1];
                adj.get(v).add(u);
            }
            for(int i=0;i<numCourses;i++){
                if(vis[i]==0){
                    if(dfs(i,adj,s1,vis,pathvis)){
                        return new int[0];
                    }
                    }
            }
            int y=0;
            while(!s1.isEmpty()){
                res[y++]=s1.pop();
            }
            return res;

        }
    }