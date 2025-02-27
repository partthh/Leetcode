class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(nums[-1]!=len(nums)):
            return len(nums)
        for i in range(len(nums)+1):
            if(nums[i]!=i):
                return i