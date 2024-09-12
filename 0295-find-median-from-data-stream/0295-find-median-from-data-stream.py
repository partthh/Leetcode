import heapq
class MedianFinder(object):

    def __init__(self):
        self.left_max=[]
        self.right_min=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.left_max or num<= -self.left_max[0]:
            heapq.heappush(self.left_max,-num)
        else:
            heapq.heappush(self.right_min,num)
        if len(self.left_max) > len(self.right_min) + 1:
            heapq.heappush(self.right_min, -heapq.heappop(self.left_max))
        elif len(self.right_min) > len(self.left_max):

            heapq.heappush(self.left_max, -heapq.heappop(self.right_min))
    def findMedian(self):
        """
        :rtype: float
        """
        if((len(self.left_max)+len(self.right_min))%2==0 ):
            return (-self.left_max[0]+self.right_min[0])/2.0
        return -self.left_max[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()