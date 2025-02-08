class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1={}
        for i ,num in enumerate(nums):
            if target-num in dict1:
                return [i,dict1[target-num]]
            dict1[num]=i
