class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set1={}
        for i in nums:
            if i in set1:
                set1[i]+=1
            else:
                set1[i]=1
        l1=[]
        for u,values in set1.items():
            con=len(nums)/3 
            if values>con:
                l1.append(u)
        return l1
