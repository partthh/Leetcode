class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=0 
        x1=""
        for i in s:
            if(i=="("):
                if count:
                    x1+=i
                count+=1
            else:
                count-=1
                if count:
                    x1+=i 
                # count-=1
            
            # elif(count>1 and i=="}"):
            #     count-=1
            #     x1.add(i)
            # else:
            #     count-=1
        return x1
        