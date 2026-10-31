class pair{
    int first;
    int w;
    pair(int first,int w){
        this.first=first;
        this.w=w;
    }
}
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        ArrayList<ArrayList<pair>> adj=new ArrayList<>();
        for(int i=0;i<n+1;i++){
            adj.add(new ArrayList<>());
        }
        int[] dist=new int[n+1];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[k]=0;
        dist[0]=0;

        for(int[] edge:times){
            int u=edge[0];
            int v=edge[1];
            int w=edge[2];
            adj.get(u).add(new pair(v,w));
        }
        PriorityQueue<pair> q1=new PriorityQueue<>((a,b)->a.w-b.w);
        q1.offer(new pair(k,0));
        while(!q1.isEmpty()){
            pair x=q1.poll();
            int node=x.first;
            int currw=x.w;
            for(pair n1:adj.get(node)){
                int total=n1.w+currw;
                if(total<dist[n1.first]){
                    dist[n1.first]=total;
                    q1.offer(new pair(n1.first,total));
                }
            }
        }
        int maxi=Integer.MIN_VALUE;
        for(int i=0;i<dist.length;i++){
            if(dist[i]==Integer.MAX_VALUE){
                return -1;
            }
            maxi=Math.max(dist[i],maxi);
        }
        return maxi;
        
    }
}