class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        maxi=0
        for i in nums:
            if i==1:
                count+=1
            else:
                if count>=maxi:
                    maxi=count
                                    
                count=0
                
        if(count>=maxi):
            maxi=count

        return maxi