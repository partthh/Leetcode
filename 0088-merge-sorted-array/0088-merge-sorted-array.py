class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr=[0]*(m+n)
        left=0 
        right=0
        index=0
        while left<m and right<n:
            if nums1[left]<=nums2[right]:
                arr[index]=nums1[left]
                left+=1
                index+=1
            else:
                arr[index]=nums2[right]
                right+=1
                index+=1
        print("1",index)
        while left<m:
            arr[index]=nums1[left]
            left+=1
            index+=1
        print("2",arr)
        while right<n:
            arr[index]=nums2[right]
            right+=1
            index+=1
        print("3",arr)
        for i in range(len(nums1)):
            nums1[i]=arr[i]