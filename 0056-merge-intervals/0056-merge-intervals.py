class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        arr=[]
        start=intervals[0][0]
        right=intervals[0][1]

        for i in range(1,len(intervals)):
            if right>=intervals[i][0]:
                right=max(intervals[i][1],right)
            else:
                arr.append([start,right])
                start=intervals[i][0]
                right=intervals[i][1]
        arr.append([start,right])
        return arr

        