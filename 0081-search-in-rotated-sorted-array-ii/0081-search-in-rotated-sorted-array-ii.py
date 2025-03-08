class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if (nums[mid]==target):
                return True
            if (nums[low]==nums[mid] and nums[mid]==nums[high]):
                low+=1
                high-=1
                continue
            if (nums[low]<=nums[mid]):
                if(target<=nums[mid] and target>=nums[low]):
                    high=mid-1
                    
                else:
                    low=mid+1
            else:
                if(target<=nums[high] and target>=nums[mid]):
                    low=mid+1
                else:
                    high=mid-1
        return False