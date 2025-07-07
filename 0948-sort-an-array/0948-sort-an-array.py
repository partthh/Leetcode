class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        low=0
        high=len(nums)-1
        self.merge_s(low,high,nums)
        return nums

       

    def merge_s(self,low,high,nums):
        if low>=high:
            return
        mid=(low+high)//2
        self.merge_s(low,mid,nums)
        self.merge_s(mid+1,high,nums)
        self.merge_m(low,mid,high,nums)
    def merge_m(self,low,mid,high,nums):
        temp=[]
        left=low
        right=mid+1
        while left<=mid and right<=high:
            if nums[left]>nums[right]:
                temp.append(nums[right])
                right+=1
            else:
                temp.append(nums[left])
                left+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for i in range(len(temp)):
            nums[low+i]=temp[i]
