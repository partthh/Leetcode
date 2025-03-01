class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1={}
        a1=[]
        for i in nums:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        for i,values in set1.items():
            con=len(nums)//2
            if(values>con):
                return i
                # a1.append(i)
            
        # return a1
        