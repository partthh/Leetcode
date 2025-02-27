class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        maxi=0
        for j in range(len(nums)):
            if nums[j]==0:
                i=j+1
            maxi=max(maxi,j-i+1)
        return maxi
        