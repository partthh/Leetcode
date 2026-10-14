class Solution {
    public boolean fun1(int i1,int[][] graph,int[] color){
        Queue<Integer> q1=new LinkedList<>();
        q1.add(i1);
        while(!q1.isEmpty()){
            int node=q1.peek();
            q1.remove();
            for(int i:graph[node]){
                if(color[i]==-1){
                    if(color[node]==1){
                        color[i]=0;
                    }
                    else{
                        color[i]=1;
                    }
                    q1.offer(i);
                }
                else if(color[i]==color[node]){
                    return false;
                }
            }
        }
        return true;
    }
    public boolean isBipartite(int[][] graph) {
        int[] color=new int[graph.length];
        Arrays.fill(color,-1);
        for(int i=0;i<graph.length;i++){
            if(color[i]==-1){
                if(fun1(i,graph,color)==false){
                    return false;
                    }
            }
        }

        return true;
    }
}