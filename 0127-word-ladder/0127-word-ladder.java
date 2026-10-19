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
        Queue<Pair> q1=new LinkedList<>();
        q1.add(new Pair(beginWord,1));
        Set<String> s1=new HashSet<>();
        for(String s:wordList){
            s1.add(s);
        }
        s1.remove(beginWord);
        while(!q1.isEmpty()){
            Pair node=q1.peek();
            q1.poll();
            String word=node.first;
            int len=node.len;
            if(word.equals(endWord)){
                return len;
            }
            for(int i=0;i<word.length();i++){
                for(char ch='a';ch<='z';ch++){
                    StringBuilder n1=new StringBuilder(word);
                    n1.setCharAt(i,ch);
                    String newword=n1.toString();
                    if(s1.contains(newword)){
                        s1.remove(newword);
                        q1.add(new Pair(newword,len+1));
                    }
                }
            }
        }
        return 0;
    }
}