class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr1=[]
        nums.sort()
        for i in range(len(nums)):
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            
            while j<k:
                sum1=nums[i]+nums[j]+nums[k]
                if sum1==0:
                    temp=[nums[i],nums[j],nums[k]]
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    arr1.append(temp)
                elif(sum1>0):
                    k-=1
                else:
                    j+=1
        return arr1
                    