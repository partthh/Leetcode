class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=float('-inf')
        
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            maxi=max(sum1,maxi)
            if sum1 <0:
                sum1=0
        return maxi