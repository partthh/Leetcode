class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre=1
        suf=1
        maxi=-float('inf')
        for i in range(len(nums)):
            if pre==0:
                pre=1
            if suf==0:
                suf=1
            pre*=nums[i]
            suf*=nums[len(nums)-i-1]
            maxi=max(maxi,max(pre,suf))
        return maxi

            