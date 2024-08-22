class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans=0
        sign=1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if(dividend<0 and divisor>0):
            sign=-1
        elif(dividend>0 and divisor <0):
            sign=-1
        n1=abs(dividend)
        n2=abs(divisor)
        while n1>=n2:
            count1=0
            while n1>=(n2<<(count1+1)):
                count1+=1
            ans+=1<<count1
            n1-=(n2<<count1)
        
        return sign *ans
            