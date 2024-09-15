import heapq 
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        num1=[]
        for i in piles:
            num1.append(-i)
        heapq.heapify(num1)
        for i in range(k):
            # count+=(i//2)
            x=-heapq.heappop(num1)
            # if(i<k):
            larg=x-(x//2)
                # count+=larg
        
            # else:
            # count+=x
            heapq.heappush(num1,-larg)
        return (-sum(num1))



        