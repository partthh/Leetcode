class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        x1=""
        if int(num[-1])%2!=0:
            return str(num[:])
        for i in range(len(num)-2,-1,-1):
            if(int(num[i])%2==1):
                return str(num[0:i+1])
        return ""