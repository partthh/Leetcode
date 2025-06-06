class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        x1=x
        x2=0
        while x1>0:
            n=x1%10
            x2=(x2*10)+n
            x1=x1//10
        return x2==x