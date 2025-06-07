class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # x1=x
        new=0
        if x>0:
            flag=1
            x1=x
        else:
            flag=0
            x1=-1*x
        while x1>0:
            new=(new*10)+(x1%10)
            x1=x1//10
        if new>2**31 or new<-2**31:
            return 0
        # elif new<-2**31:
        #     return 0
        else:

            if flag:
                return new
            else:
                return (-1*new)
        # for i in range(len(str(new))):
        #     if new[i]=="0":

