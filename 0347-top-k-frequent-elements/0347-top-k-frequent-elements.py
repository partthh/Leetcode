import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l1=[]
        x1=Counter(nums)
        for i in range(k):
            max1=max(x1,key=x1.get)
            l1.append(max1)
            del x1[max1]
        return l1

        
        

        