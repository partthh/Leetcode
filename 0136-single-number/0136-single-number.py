class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        hashset={}
        for i in range(n):
            if(nums[i] in hashset):
                hashset[nums[i]]+=1
            else:
                hashset[nums[i]]=1
        for key,value in hashset.items():
            if(value==1):
                return key       