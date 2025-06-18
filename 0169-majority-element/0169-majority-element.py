from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1=Counter(nums)
        for i,j in dict1.items():
            if 2*j>len(nums):
                return i