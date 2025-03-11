class Solution:
    def frequencySort(self, s: str) -> str:
        # s="Aabb"
        set1={}
        for i in s:
            if( i in set1):
                set1[i]+=1
            else:
                set1[i]=1
        s1=dict(sorted(set1.items(),key=lambda item:item[1] ,reverse=True))
        s2=""
        for i,j in s1.items():
            while j!=0:
                s2+=i
                j-=1
        return(s2)