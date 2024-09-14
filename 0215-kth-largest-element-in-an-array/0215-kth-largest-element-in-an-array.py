import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums1=[]
        # for i in nums:
        #     nums1.append(-i)
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)

        return(heapq.heappop(nums))

        