class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dip=0
        n=len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)% n] :
                dip+=1
        if dip==0:
            return True
        elif(dip==1):
            return True
        else:
            return False        