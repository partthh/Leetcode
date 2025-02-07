class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        arr=[0]*(n+1)
        for i in range(n):
            arr[nums[i]]+=1

        for i in range(0,n+1):
            if(arr[i]==0):
                return i
