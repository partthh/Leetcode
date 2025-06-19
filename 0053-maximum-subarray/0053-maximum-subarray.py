class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        sum1=0
        maxi=-float('inf')
        for i in nums:
            sum1+=i
            maxi=max(maxi,sum1)
            if sum1<0:
                sum1=0
        return maxi