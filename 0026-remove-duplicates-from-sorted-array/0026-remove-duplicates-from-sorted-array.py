class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        for k in range(1,len(nums)):
            if(nums[i]==nums[j]):
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                j+=1
        return i+1
            

            