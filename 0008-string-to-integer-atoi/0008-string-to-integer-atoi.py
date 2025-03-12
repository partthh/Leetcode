class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX=2**31-1
        INT_MIN=-2**31
        i=0
        n=len(s)
        while i<n and s[i]==" ":
            i+=1
        sign=1
        if i<n and s[i]=="-":
            sign=-1
            i+=1
        elif(i<n and s[i]=="+"):
            sign=+1
            i+=1
        result=0
        while i<n and s[i].isdigit():
            if result>(INT_MAX-int(s[i]))//10:
                if sign==1:
                    return INT_MAX
                else:
                    return INT_MIN


            result=result*10+int(s[i])
            i+=1
        return sign*result