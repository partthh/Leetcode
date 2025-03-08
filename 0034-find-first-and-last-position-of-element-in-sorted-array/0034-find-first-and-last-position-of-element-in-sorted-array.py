class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def Upper(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if (nums[mid]==target):
                    ans=mid
                    low=mid+1
                elif(nums[mid]>target):
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def Lower(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if (nums[mid]==target):
                    ans=mid
                    high=mid-1
                elif(nums[mid]>target):
                    high=mid-1
                else:
                    low=mid+1
            return ans
        x1=Upper(nums,target)
        x2=Lower(nums,target)

        return [x2,x1]