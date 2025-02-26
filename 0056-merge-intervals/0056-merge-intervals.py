class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        left=intervals[0][0]
        right=intervals[0][1]
        arr1=[]
        for i in range(1,len(intervals)):
            if(right>=intervals[i][0]):
                right=max(right,intervals[i][1])
            else:
                arr1.append([left,right])
                left=intervals[i][0]
                
                right=intervals[i][1]
        arr1.append([left,right])
        return arr1