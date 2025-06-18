class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        ele=nums[0]
        for i in range(1,len(nums)):
            if count==0:
                ele=nums[i]
                count+=1
            elif(nums[i]==ele):
                count+=1
            else:
                count-=1
        return ele