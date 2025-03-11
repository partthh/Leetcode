class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        set1={}
        set2={}
        for s_el,t_el in zip(s,t):
            if (s_el in set1 and set1[s_el]!=t_el) or (t_el in set2 and set2[t_el]!=s_el) :
                return False
            
            set1[s_el]=t_el
            set2[t_el]=s_el
        # if x1==t:
        return True
        # return False
        