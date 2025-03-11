class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n=0
        
        while n!=len(s):
            s=list(s)
            a1=s[0]
            for i in range(1,len(s)):
                s[i-1]=s[i]
            s[-1]=a1
            s="".join(s)
            if s==goal:
                return True
            n+=1 

        return False