class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        len1=len(nums)
        for i in range(len(nums)):
                # print(i)
                if(nums[i]!=0):
                    # print(nums)
                    nums.append(nums[i])
                    # del nums[i]
                else:
                    count+=1
        for i in range(count):
            nums.append(0)
        for i in range(len1):
            nums.pop(0)