class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=0
        neg=1
        arr1=[0]*len(nums)
        for i in nums:
            if i>0:
                arr1[pos]=i
                pos+=2
            else:
                arr1[neg]=i
                neg+=2
        return arr1