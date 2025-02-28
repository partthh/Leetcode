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
        for k in range(len(nums)-2):
            left=k+1
            right=len(nums)-1
            # print(k, left, right)
            while left<right:
                # print( left, right)
                if nums[left]+nums[right]+nums[k]== 0:
                    if([nums[left],nums[right],nums[k]] not in l1):

                        l1.append([nums[left],nums[right],nums[k]])
                    left+=1
                    # break
                elif nums[left]+nums[right]+nums[k]>0:
                    right-=1
                else:
                    left+=1
            # while k<=len(nums)-3 and nums[k]==nums[k+1]:
                # k+=1
        return l1
