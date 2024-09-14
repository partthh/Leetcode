import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums1=[]
        for i in nums:
            nums1.append(-i)
        heapq.heapify(nums1)
        for i in range(k-1):
            heapq.heappop(nums1)

        return(-heapq.heappop(nums1))

        