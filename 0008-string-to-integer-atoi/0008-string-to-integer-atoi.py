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
            result=result*10+int(s[i])
            if result*sign>INT_MAX:
                return INT_MAX
            if result*sign<INT_MIN: 
                return INT_MIN
            i+=1
        return sign*result