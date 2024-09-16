import heapq


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        l1 = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        
        l1.sort(key=lambda x: x[0])
        
        result=[]
        heap=[] #isme se hum pop kreneg /isme push krenge
        time=0   
        i=0
        n=len(tasks)
        while len(result) < n:
            while i < n and l1[i][0] <= time:
                heapq.heappush(heap, (l1[i][1], l1[i][2]))  # (processingTime, index)
                i += 1
            
            if heap:
                processing, index = heapq.heappop(heap)
                time += processing  
                result.append(index) 
            else:
                time = l1[i][0]
        
        return result
