class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        for i in range(len(nums)):
            l1=[]
            sum1=0
            sum1+=nums[i]
            l1.append(i)
            for j in range(i+1,len(nums)):
                sum1+=nums[j]

                if sum1==target:
                    l1.append(j)
                    return l1
                else:
                    sum1-=nums[j]