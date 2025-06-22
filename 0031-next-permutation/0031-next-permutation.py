class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                x=i
                print(x)
                break

        if x==-1:
            nums.reverse()
            return nums
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[x]<nums[i]:
                    nums[x],nums[i]=nums[i],nums[x]
                    break
            nums[x+1:]=reversed(nums[x+1:])