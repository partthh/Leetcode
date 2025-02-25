class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=1
        sufix=1
        maxi=float('-inf')
        for i in range(len(nums)):
            if prefix==0:
                prefix=1
            if sufix==0:
                sufix=1
            prefix*=nums[i]
            sufix*=nums[len(nums)-i-1]
            maxi=max(maxi,max(prefix,sufix))
        return maxi

