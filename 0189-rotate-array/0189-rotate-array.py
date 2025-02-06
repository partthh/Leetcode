class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=(len(nums)-k)%len(nums)
        pos=0
        arr1=[]
        for i in range(k):
            arr1.append(nums[i])
        for i in range(k,len(nums)):
            nums[pos]=nums[i]
            pos+=1
        a=0
        for i in range(len(nums)-k,len(nums)):
            nums[i]=arr1[a]
            a+=1