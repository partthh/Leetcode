class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mid=0
        high=len(nums)-1
        low=0
        while mid<=high:
            # if nums[low]==2:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif(nums[mid]==2):
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            else:
                mid+=1
            # if nums[low]==2:
                # nums[high],nums[low]=nums[low],nums[high]
                # high-=1
            # elif (nums[low]==0):
                # low+=1
            # elif (nums[high]==0):
                # nums[high],nums[low]=nums[low],nums[high]
                # low+=1
            # elif(nums[low]==1):
                # low+=1
            
