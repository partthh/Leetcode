class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        set1={}
        for i in s:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for i in t:
            if i not in set1:
                return False
            else:
                set1[i]-=1
        for i in s:
            if set1[i]!=0:
                return False
        return True 