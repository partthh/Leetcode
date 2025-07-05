class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr=[]
        k=m-1
        l=0
        while k>=0 and l<n:
            if nums2[l]<nums1[k]:
                nums2[l],nums1[k]=nums1[k],nums2[l]
                k-=1
                l+=1
            else:
                break
        nums1[0:m]=sorted(nums1[0:m])
        nums2.sort()
        p=0
        for i in range(m,len(nums1)):

            nums1[i]=nums2[p]
            p+=1
        