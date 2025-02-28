class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # i=0
        # j=len(nums)-1
        l1=[]
        nums.sort()
        for k in range(len(nums)):
            if k!=0 and nums[k]==nums[k-1]:
                continue
            left=k+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[k]== 0:

                    l1.append([nums[left],nums[right],nums[k]])
                     
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif (nums[left]+nums[right]+nums[k]>0):
                        right-=1
                else:
                        left+=1

        return l1
