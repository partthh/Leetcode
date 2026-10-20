class pair{
    int first;
    int second;
    pair(int first,int second){
        this.first=first;
        this.second=second;
    }
}
class pair1{
    int steps;
    int node;
    int distance;
    pair1(int steps,int node,int distance){
        this.steps=steps;
        this.node=node;
        this.distance=distance;
    }
}
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        ArrayList<ArrayList<pair>> adj=new ArrayList<>();
        for(int i=0;i<n;i++){
            adj.add(new ArrayList<>());
        }
        for(int i=0;i<flights.length;i++){
            int u=flights[i][0];
            int v=flights[i][1];
            adj.get(u).add(new pair(v,flights[i][2]));
        }
        int[] dist=new int[n];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[src]=0;
        Queue<pair1> q1=new LinkedList<>();
        q1.add(new pair1(0,src,0));
        int level=0;
        while(!q1.isEmpty() && level<=k){
            int size=q1.size();
            for(int i=0;i<size;i++){
                pair1 x=q1.poll();
                int s1=x.steps;
                int node=x.node;
                int distance=x.distance;

                for(pair edge:adj.get(node)){
                    int price=edge.second;
                    int n1=edge.first;
                    if(distance+price<dist[n1]){
                        dist[n1]=distance+price;
                        q1.add(new pair1(s1+1,n1,distance+price));
                    }
                }
            }
            level++;
        }
        
        if(dist[dst]!=Integer.MAX_VALUE){
            return dist[dst];
        }
        else{
            return -1;
        }
        
}
}