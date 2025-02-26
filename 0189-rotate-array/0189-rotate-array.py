class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        k=(n-k)%n
        arr=[]
        pos=0
        for i in range(k):
            arr.append(nums[i])
        for i in range(k,n):
            nums[pos]=nums[i]
            pos+=1
        pos=0
        for i in range(n-k,n):
            nums[i]=arr[pos]
            pos+=1