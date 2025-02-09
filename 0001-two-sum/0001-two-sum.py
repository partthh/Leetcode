class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # set1=dict{}
        # rem=0
        for i in range(len(nums)):
            rem=0
            for j in range(i+1,len(nums)):
                rem=target-nums[i]
                if rem ==nums[j]:
                    return [i,j]
                    

