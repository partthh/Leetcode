class Solution:
    def maxDepth(self, s: str) -> int:
        if s=="":
            return 0
        count=0 
        maxi=0
        for i in s:
            if(i=="("):
                count+=1
                maxi=max(count,maxi)
            elif (i==")"):
                count-=1
        return maxi
        