class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1=s.split()
        l1.reverse()
        ans=" ".join(l1)
        return ans
        
        