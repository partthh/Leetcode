class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1=str(x)
        x2=""
        for i in range (len(x1)-1,-1,-1):
            x2+=x1[i]
        print(x2)
        if x1==(x2):
            return True
        else:
            return False