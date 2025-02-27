class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=(len(nums)*(len(nums)+1))/2
        sum2=0
        for i in range(len(nums)):
            sum2=sum2+nums[i]
        return sum1-sum2