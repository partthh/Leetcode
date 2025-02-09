class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        inde=-1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                inde=i
                break
        if inde==-1:
            nums.reverse()
            return nums
        else:
            for i in range(len(nums)-1,i,-1):
                if nums[i]>nums[inde]:
                    nums[i],nums[inde]=nums[inde],nums[i]
                    break
            nums[inde+1:]=reversed(nums[inde+1:])

        