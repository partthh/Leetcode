class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [
            (1000, 'M'), 
            (900, 'CM'), 
            (500, 'D'), 
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')]
        result=""
        
        result = ""
        for value, symbol in values:
            while num >= value:  
                num -= value
                result += symbol  
        return result











        # while num!=0:
        #     min1=0
        #     count1=0
        #     roman=""
        #     for i,j in values:
        #         if (i<num):

        #             if(min1<i):
        #                 min1=i
        #                 roman=j
                    
        #     while num>=min1:
        #         num=num//min1
        #         count1+=1
        #     str1+=*count1
        #     num=num%min1


            