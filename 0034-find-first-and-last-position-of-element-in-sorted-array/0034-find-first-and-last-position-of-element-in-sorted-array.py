class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFloor(nums, target):
        #Your code here
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if(nums[mid]==target):
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                    
                else:
                    # ans=mid
                    high=mid-1
            return ans
        def ceil(nums,target):
            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if(nums[mid]==target):
                    ans=mid
                    low=mid+1
                elif(nums[mid]<target):
                    low=mid+1
                else:
                    high=mid-1
            return ans
        x1=findFloor(nums,target)
        x2=ceil(nums,target)
        # if x1==len(nums) or nums[x1]!=target :
            # return [-1,-1]
        # else:
        return[x1,x2]
        # return [x1,x2]