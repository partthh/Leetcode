class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1={}
        for i in nums:
            
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for key,value in set1.items():
            if value==1:
                return key