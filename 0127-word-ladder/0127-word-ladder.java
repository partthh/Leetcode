class Pair{
    String first;
    int len;
    Pair(String first,int len){
        this.first=first;
        this.len=len;
    }
}
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> s1=new HashSet<>();
        for(String x:wordList){
            s1.add(x);
        }
        Queue<Pair> q1=new LinkedList<>();
        q1.offer(new Pair(beginWord,1));
        s1.remove(beginWord);
        while(!q1.isEmpty()){
            Pair a=q1.poll();
            String node=a.first;
            int len=a.len;
            if(node.equals(endWord)){
                return len;
            }
            for(int i=0;i<node.length();i++){
                for(char j='a';j<='z';j++){
                    StringBuilder sb=new StringBuilder(node);
                    sb.setCharAt(i,j);
                    String newword=sb.toString();
                    if(s1.contains(newword)){
                        q1.offer(new Pair(newword,len+1));
                        s1.remove(newword);
                    }
                }
            }
            
        }
        return 0;
    }
}