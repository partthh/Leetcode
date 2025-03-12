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
        while num!=0:
            min1=0
            x1=0
            value1=""
            for i,j in values:
                if i<=num:

                    min1=i
                    value1=j
                    break
            x1=num//min1
            num=num%min1
            result+=value1*x1
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


            