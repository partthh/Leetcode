class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        set1=set(nums)
        maxi=0
        longi=0
        for i in set1:
            x=i
            if x-1 not in set1:
                longi=1
                while x+1 in set1 :
                    longi+=1
                    x+=1
                maxi=max(maxi,longi)
        return maxi
        