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
        for i,f in x1.most_common(k):
            l1.append(i)
        return l1

        
        

        