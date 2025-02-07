class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum1=n*(n+1)/2
        sum2=0
        for i in range(len(nums)):
            sum2+=nums[i]
        return sum1-sum2
        